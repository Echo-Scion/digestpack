import os
import sys
import unittest
import tempfile
import shutil

# Ensure .agents/scripts is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from digestpack.dna import classify_file_to_tier
from digestpack.packer import (
    is_foundation_root,
    is_audit_worthy,
    ContextPacker,
    DEFAULT_IGNORE_FILENAMES,
    DEFAULT_IGNORE_DIRS,
    export_audit_bundles,
)


class TestUniversalPacker(unittest.TestCase):
    def test_foundation_detection(self):
        with tempfile.TemporaryDirectory() as td:
            with open(os.path.join(td, "VERSION"), "w") as f:
                f.write("0.0.1")
            os.makedirs(os.path.join(td, ".agents", "rules"))
            os.makedirs(os.path.join(td, ".agents", "scripts", "core"))
            with open(os.path.join(td, ".agents", "scripts", "orion.py"), "w") as f:
                f.write("print('orion')")
            self.assertTrue(is_foundation_root(td))

            self.assertFalse(is_foundation_root("tools/flutterin"))

    def test_classify_app_file(self):
        self.assertEqual(classify_file_to_tier("package.json")[0], "0_pillars_and_manifests")
        self.assertEqual(classify_file_to_tier("src/models/user.ts")[0], "1_contracts")
        self.assertEqual(classify_file_to_tier("src/services/api.ts")[0], "3_services")
        self.assertEqual(classify_file_to_tier("src/controllers/auth.ts")[0], "4_state")
        self.assertEqual(classify_file_to_tier("src/ui/Button.tsx")[0], "5_presentation")

    def test_ignore_lists(self):
        self.assertIn("package-lock.json", DEFAULT_IGNORE_FILENAMES)
        self.assertIn("yarn.lock", DEFAULT_IGNORE_FILENAMES)
        self.assertIn("pubspec.lock", DEFAULT_IGNORE_FILENAMES)
        self.assertIn("scratch", DEFAULT_IGNORE_DIRS)
        self.assertIn("node_modules", DEFAULT_IGNORE_DIRS)

    def test_is_audit_worthy_lean_vs_all(self):
        # App project lean excludes docs and examples
        self.assertFalse(is_audit_worthy("docs/intro.md", mode="lean"))
        self.assertFalse(is_audit_worthy("examples/sample.json", mode="lean"))
        self.assertFalse(is_audit_worthy("tests/test_api.py", mode="lean"))
        self.assertTrue(is_audit_worthy("src/index.ts", mode="lean"))

        # App project all includes docs and examples
        self.assertTrue(is_audit_worthy("docs/intro.md", mode="all"))
        self.assertTrue(is_audit_worthy("examples/sample.json", mode="all"))
        self.assertTrue(is_audit_worthy("tests/test_api.py", mode="all"))

    def test_export_gemini_bundles_temp_dir(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a mock application
            os.makedirs(os.path.join(temp_dir, "src", "core"))
            os.makedirs(os.path.join(temp_dir, "bin"))
            os.makedirs(os.path.join(temp_dir, "scratch"))

            with open(os.path.join(temp_dir, "package.json"), "w") as f:
                f.write('{"name": "mock-app"}')
            with open(os.path.join(temp_dir, "src", "core", "domain.ts"), "w") as f:
                f.write("export interface MockDomain { id: string; }")
            with open(os.path.join(temp_dir, "bin", "cli.ts"), "w") as f:
                f.write("console.log('cli');")
            # This should be ignored by DEFAULT_IGNORE_FILENAMES
            with open(os.path.join(temp_dir, "package-lock.json"), "w") as f:
                f.write('{"lockfileVersion": 3}')
            # This should be ignored by DEFAULT_IGNORE_DIRS
            with open(os.path.join(temp_dir, "scratch", "junk.txt"), "w") as f:
                f.write("junk data")

            out_dir = os.path.join(temp_dir, "export")
            bundles = export_audit_bundles(temp_dir, out_dir=out_dir, num_bundles=10, mode="lean")

            self.assertTrue(len(bundles) >= 2)
            for b in bundles:
                with open(b, "r", encoding="utf-8") as bf:
                    content = bf.read()
                self.assertNotIn("package-lock.json", content)
                self.assertNotIn("junk.txt", content)

    def test_skeletonize_python(self):
        from digestpack.packer import skeletonize_code
        code = '''import os\n\ndef add(a: int, b: int) -> int:\n    """Adds two integers."""\n    res = a + b\n    return res\n\nclass Calculator:\n    """Simple calc."""\n    def multiply(self, x: int, y: int) -> int:\n        return x * y\n'''
        skel = skeletonize_code(code, "py")
        self.assertIn("def add(a: int, b: int) -> int:", skel)
        self.assertIn("class Calculator:", skel)
        self.assertIn("Simple calc.", skel)
        self.assertIn("[Body omitted for audit", skel)
        self.assertNotIn("res = a + b", skel)

    def test_skeletonize_c_like(self):
        from digestpack.packer import skeletonize_code
        ts_code = 'export interface User { id: string; }\nexport class ApiService {\n    async getData() {\n        return await fetch("/api");\n    }\n}'
        skel = skeletonize_code(ts_code, "ts")
        self.assertIn("export interface User", skel)
        self.assertIn("export class ApiService", skel)
        self.assertIn("[Implementation omitted for audit]", skel)

    def test_add_line_numbers_and_dynamic_fence(self):
        from digestpack.packer import add_line_numbers, get_dynamic_fence
        content = "line one\nline two\nline three"
        numbered = add_line_numbers(content)
        self.assertIn("  1 | line one", numbered)
        self.assertIn("  2 | line two", numbered)
        self.assertIn("  3 | line three", numbered)

        # Dynamic fence check
        fence = get_dynamic_fence("regular code")
        self.assertEqual(fence, "```")
        nested_fence = get_dynamic_fence("nested ``` markdown")
        self.assertEqual(nested_fence, "````")

    def test_calculate_token_stats(self):
        from digestpack.scanner import calculate_token_stats
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, "test.py"), "w", encoding="utf-8") as f:
                f.write("print('hello world')\n")
            with open(os.path.join(temp_dir, "doc.md"), "w", encoding="utf-8") as f:
                f.write("# Title\n")
            stats = calculate_token_stats(temp_dir, ["test.py", "doc.md"])
            self.assertEqual(stats["total_files"], 2)
            self.assertIn(".py", stats["by_extension"])
            self.assertIn(".md", stats["by_extension"])
            self.assertTrue(stats["total_tokens"] > 0)

    def test_render_prompt_template(self):
        from digestpack.packer import render_prompt_template
        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tf:
            tf.write("SYSTEM ARCHITECTURE & SECURITY AUDIT PROMPT\nRepository: {{repo_name}}\n{{files}}")
            tf_name = tf.name
        try:
            ctx = {"repo_name": "test_repo", "file_count": 5, "token_count": 100, "tree": "src/", "files": "dummy files"}
            rendered = render_prompt_template(tf_name, ctx)
            self.assertIn("SYSTEM ARCHITECTURE & SECURITY AUDIT PROMPT", rendered)
            self.assertIn("Repository: test_repo", rendered)
            self.assertIn("dummy files", rendered)
        finally:
            if os.path.exists(tf_name):
                os.remove(tf_name)

    def test_pack_claude_xml(self):
        from digestpack.packer import ContextPacker
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, "test.py"), "w", encoding="utf-8") as f:
                f.write("x = 42\n")
            packer = ContextPacker(temp_dir)
            digest = packer.pack_digest(["test.py"])
            self.assertIn('<artifact index="1"', digest)
            self.assertIn('path="test.py"', digest)
            self.assertIn("x = 42", digest)
            self.assertIn("</artifact>", digest)

    def test_vibe_intent_audit(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, "main.py"), "w", encoding="utf-8") as f:
                f.write("def run():\n    pass\n")
            out_dir = os.path.join(temp_dir, "audit_out")
            bundles = export_audit_bundles(temp_dir, out_dir=out_dir, skeleton=True, line_numbers=True)
            self.assertTrue(len(bundles) >= 1)
            with open(bundles[0], "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("def run():", content)

    def test_audit_full_vs_skeleton_vs_hybrid(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            core_dir = os.path.join(temp_dir, "core")
            cli_dir = os.path.join(temp_dir, "cli")
            os.makedirs(core_dir, exist_ok=True)
            os.makedirs(cli_dir, exist_ok=True)

            with open(os.path.join(core_dir, "models.py"), "w", encoding="utf-8") as f:
                f.write("def calculate_total(a, b):\n    result = a + b\n    return result\n")
            with open(os.path.join(cli_dir, "commands.py"), "w", encoding="utf-8") as f:
                f.write("def cli_entrypoint():\n    print('CLI running')\n    sys.exit(0)\n")

            # 1. Full Audit (default): bodies are 100% preserved
            out_full = os.path.join(temp_dir, "out_full")
            bundles_full = export_audit_bundles(temp_dir, out_dir=out_full, skeleton=False, line_numbers=True)
            full_texts = []
            for b in bundles_full:
                with open(b, "r", encoding="utf-8") as f:
                    full_texts.append(f.read())
            combined_full = "\n".join(full_texts)
            self.assertIn("result = a + b", combined_full)
            self.assertIn("print('CLI running')", combined_full)
            self.assertNotIn("[Body omitted for audit", combined_full)

            # 2. Skeleton Audit: bodies are collapsed into signatures
            out_skel = os.path.join(temp_dir, "out_skel")
            bundles_skel = export_audit_bundles(temp_dir, out_dir=out_skel, skeleton=True, line_numbers=True)
            skel_texts = []
            for b in bundles_skel:
                with open(b, "r", encoding="utf-8") as f:
                    skel_texts.append(f.read())
            combined_skel = "\n".join(skel_texts)
            self.assertIn("[Body omitted for audit", combined_skel)

            # 3. Hybrid Audit: Core execution bundles (01-07) full, governance/docs (08-10) condensed
            out_hybrid = os.path.join(temp_dir, "out_hybrid")
            bundles_hybrid = export_audit_bundles(temp_dir, out_dir=out_hybrid, skeleton=False, line_numbers=True, hybrid=True)
            hybrid_texts = {}
            for b in bundles_hybrid:
                with open(b, "r", encoding="utf-8") as f:
                    hybrid_texts[os.path.basename(b)] = f.read()
            core_bundle = next((v for k, v in hybrid_texts.items() if "CORE" in k or 'path="core/models.py"' in v), "")
            cli_bundle = next((v for k, v in hybrid_texts.items() if "CLI" in k or 'path="cli/commands.py"' in v), "")
            self.assertIn("result = a + b", core_bundle)
            self.assertIn("print('CLI running')", cli_bundle)

    def test_skeleton_syntax_validity_py_compile(self):
        """TEST-01: Skeleton of try/except and long variables compiles without SyntaxError."""
        import py_compile
        try:
            from digestpack.scanner import skeletonize_python
        except ImportError:
            from core.scanner import skeletonize_python
        code = '''
import os
import sys

try:
    from core.security import sanitize_text, SECRET_PATTERNS
except ImportError:
    try:
        from .security import sanitize_text, SECRET_PATTERNS
    except Exception:
        SECRET_PATTERNS = [
            ("KEY_1", "val1"),
            ("KEY_2", "val2"),
            ("KEY_3", "val3"),
            ("KEY_4", "val4"),
            ("KEY_5", "val5"),
            ("KEY_6", "val6"),
        ]

LONG_CONFIG = {
    "key1": "val1",
    "key2": "val2",
    "key3": "val3",
    "key4": "val4",
    "key5": "val5",
    "key6": "val6",
}

class SampleService:
    """Service docstring."""
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None

    def init_schema(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE
            )
        """)

    def run(self, flag: bool = True):
        # Implementation to omit
        x = 100
        return x * 2
'''
        skel = skeletonize_python(code, include_line_numbers=False)
        self.assertIn("self.db_path = db_path", skel)
        self.assertIn("CREATE TABLE IF NOT EXISTS users", skel)
        self.assertIn("SQL: CREATE users", skel)
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as tf:
            tf.write(skel)
            tf_name = tf.name
        try:
            py_compile.compile(tf_name, doraise=True)
        finally:
            if os.path.exists(tf_name):
                os.remove(tf_name)

    def test_source_true_line_numbers(self):
        """TEST-02: Skeletonized code retains true original line numbers (deviation 0)."""
        try:
            from digestpack.scanner import skeletonize_python
        except ImportError:
            from core.scanner import skeletonize_python
        code = "import os\n\n\ndef add(a, b):\n    return a + b\n\n\nclass Calc:\n    def mul(self, a, b):\n        return a * b\n"
        skel = skeletonize_python(code, include_line_numbers=True)
        lines = skel.splitlines()
        
        # Line 4 should be def add
        add_line = next((l for l in lines if "def add(a, b):" in l), "")
        self.assertTrue(add_line.startswith("   4 | "))

        # Line 8 should be class Calc:
        calc_line = next((l for l in lines if "class Calc:" in l), "")
        self.assertTrue(calc_line.startswith("   8 | "))

    def test_foundation_bundle_07_and_09_routing(self):
        """TEST-03: Classification of core memory and state machine files."""
        self.assertEqual(classify_file_to_tier(".agents/scripts/core/memory.py")[0], "3_services")
        self.assertEqual(classify_file_to_tier(".agents/scripts/core/orion_graph.py")[0], "3_services")
        self.assertEqual(classify_file_to_tier(".agents/scripts/commands/reflexion.py")[0], "8_native_and_cli")
        self.assertEqual(classify_file_to_tier(".agents/scripts/commands/state_machine.py")[0], "8_native_and_cli")

    def test_cmd_extension_included(self):
        """TEST-04: .cmd extension included in DEFAULT_TEXT_EXTENSIONS."""
        from digestpack.packer import DEFAULT_TEXT_EXTENSIONS
        self.assertIn(".cmd", DEFAULT_TEXT_EXTENSIONS)

    def test_bundle_file_inventory_table(self):
        """TEST-05: pack_digest generates Bundle File Inventory, <artifact> envelopes, and Auditor Sandbox rule."""
        with tempfile.TemporaryDirectory() as td:
            with open(os.path.join(td, "alpha.py"), "w", encoding="utf-8") as f:
                f.write("def alpha():\n    pass\n")
            with open(os.path.join(td, "beta.ts"), "w", encoding="utf-8") as f:
                f.write("export const beta = 10;\n")
            packer = ContextPacker(td)
            digest = packer.pack_digest(["alpha.py", "beta.ts"], bundle_name="TEST_BUNDLE")
            self.assertIn("## Bundle File Inventory", digest)
            self.assertIn("| 1 | `alpha.py` |", digest)
            self.assertIn("| 2 | `beta.ts` |", digest)
            self.assertIn("- Domain Bundle: TEST_BUNDLE", digest)
            self.assertIn("[AUDITOR SANDBOX RULE]", digest)
            self.assertIn('<artifact index="1" path="alpha.py"', digest)
            self.assertIn("</artifact>", digest)

    def test_directive_quarantine_and_pre_audit_radar(self):
        """TEST-06: Neutralizes prompt tags (<system-instruction>, <route>) and emits Pre-Computed Static Audit Radar."""
        from digestpack.packer import neutralize_prompt_tags, generate_bundle_pre_audit_radar
        raw = "Hello <system-instruction>hijack</system-instruction> and <route>target</route>"
        cleaned = neutralize_prompt_tags(raw)
        self.assertIn("&lt;system-instruction&gt;", cleaned)
        self.assertIn("&lt;/system-instruction&gt;", cleaned)
        self.assertIn("&lt;route&gt;", cleaned)

        with tempfile.TemporaryDirectory() as td:
            py_file = os.path.join(td, "risky.py")
            with open(py_file, "w", encoding="utf-8") as fh:
                fh.write("import subprocess\ndef run_cmd():\n    try:\n        subprocess.run(['ls'])\n    except Exception:\n        pass\n")
            radar = generate_bundle_pre_audit_radar(td, ["risky.py"])
            self.assertIn("Pre-Computed Static Audit Radar", radar)
            self.assertIn("subprocess.run()", radar)
            self.assertIn("except Exception:", radar)

    def test_tier_output_subfolders_isolation(self):
        """TEST-07: Verifies that Tier 1 (arch), Tier 2 (hybrid), and Tier 3 (full) default to distinct subfolders."""
        with tempfile.TemporaryDirectory() as td:
            with open(os.path.join(td, "main.py"), "w", encoding="utf-8") as fh:
                fh.write("def calculate(x):\n    return x * 2\n")

            # 1. Tier 1: Arch
            arch_bundles = export_audit_bundles(td, out_dir=None, skeleton=True, hybrid=False, mode="lean")
            self.assertTrue(len(arch_bundles) >= 1)
            self.assertTrue(any(os.path.normpath(".orion/bundles/arch") in os.path.normpath(b) for b in arch_bundles))

            # 2. Tier 2: Hybrid
            hybrid_bundles = export_audit_bundles(td, out_dir=None, skeleton=False, hybrid=True, mode="lean")
            self.assertTrue(len(hybrid_bundles) >= 1)
            self.assertTrue(any(os.path.normpath(".orion/bundles/hybrid") in os.path.normpath(b) for b in hybrid_bundles))

            # 3. Tier 3: Full
            full_bundles = export_audit_bundles(td, out_dir=None, skeleton=False, hybrid=False, mode="all")
            self.assertTrue(len(full_bundles) >= 1)
            self.assertTrue(any(os.path.normpath(".orion/bundles/full") in os.path.normpath(b) for b in full_bundles))

            # Verify all three subdirectories coexist simultaneously
            arch_dir = os.path.join(td, ".orion", "bundles", "arch")
            hybrid_dir = os.path.join(td, ".orion", "bundles", "hybrid")
            full_dir = os.path.join(td, ".orion", "bundles", "full")
            self.assertTrue(os.path.isdir(arch_dir))
            self.assertTrue(os.path.isdir(hybrid_dir))
            self.assertTrue(os.path.isdir(full_dir))


if __name__ == "__main__":
    unittest.main()


