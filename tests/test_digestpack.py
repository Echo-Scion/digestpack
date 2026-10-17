import os
import sys
import unittest
import tempfile

# Ensure digestpack is importable
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from digestpack.security import sanitize_text, SecurityAuditor, find_ast_grep
from digestpack.scanner import (
    skeletonize_code,
    skeletonize_python,
    calculate_token_stats,
    build_repo_map,
    extract_file_symbols,
)
from digestpack.dna import classify_file_to_tier
from digestpack.packer import (
    ContextPacker,
    export_audit_bundles,
    add_line_numbers,
    get_dynamic_fence,
    render_prompt_template,
    generate_ascii_tree,
    DEFAULT_TEXT_EXTENSIONS,
)


class TestDigestpack(unittest.TestCase):
    def test_sanitize_text(self):
        text = "My AWS key is AKIA1234567890ABCDEF and secret token"
        clean, warnings = sanitize_text(text)
        self.assertNotIn("AKIA1234567890ABCDEF", clean)
        self.assertIn("[REDACTED_AWS_KEY]", clean)
        self.assertTrue(len(warnings) > 0)

    def test_skeletonize_python(self):
        code = '''def calculate_total(items: list) -> int:
    """Calculates total sum."""
    total = 0
    for item in items:
        total += item
    return total

class Store:
    def checkout(self):
        return True
'''
        skel = skeletonize_code(code, "py")
        self.assertIn("def calculate_total(items: list) -> int:", skel)
        self.assertIn("class Store:", skel)
        self.assertIn("[Body omitted for audit", skel)
        self.assertNotIn("total += item", skel)

    def test_skeletonize_polyglot(self):
        code = '''export interface User { id: string; }
export class UserService {
    async getUser(id: string) {
        return await fetch("/api/user/" + id);
    }
}
'''
        skel = skeletonize_code(code, "ts")
        self.assertIn("export interface User", skel)
        self.assertIn("export class UserService", skel)
        self.assertIn("[Implementation omitted for audit]", skel)

    def test_line_numbers_and_dynamic_fence(self):
        content = "first line\nsecond line"
        numbered = add_line_numbers(content)
        self.assertIn("1 | first line", numbered)
        self.assertIn("2 | second line", numbered)

        fence = get_dynamic_fence("normal text")
        self.assertEqual(fence, "```")
        nested_fence = get_dynamic_fence("nested ``` code")
        self.assertEqual(nested_fence, "````")

    def test_calculate_token_stats(self):
        with tempfile.TemporaryDirectory() as td:
            with open(os.path.join(td, "main.py"), "w", encoding="utf-8") as f:
                f.write("print('hello')\n")
            with open(os.path.join(td, "README.md"), "w", encoding="utf-8") as f:
                f.write("# Hello\n")
            stats = calculate_token_stats(td, ["main.py", "README.md"])
            self.assertEqual(stats["total_files"], 2)
            self.assertIn(".py", stats["by_extension"])
            self.assertIn(".md", stats["by_extension"])
            self.assertTrue(stats["total_tokens"] > 0)

    def test_export_audit_bundles(self):
        with tempfile.TemporaryDirectory() as td:
            with open(os.path.join(td, "package.json"), "w") as f:
                f.write('{"name": "test"}')
            with open(os.path.join(td, "app.py"), "w") as f:
                f.write("def run():\n    pass\n")
            out_d = os.path.join(td, "bundles")
            bundles = export_audit_bundles(td, out_dir=out_d, skeleton=True, line_numbers=True)
            self.assertTrue(len(bundles) >= 1)
            with open(bundles[0], "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("AUDIT MANIFESTO", content)

    def test_extract_file_symbols_polyglot_and_python_standalone(self):
        """Verify extract_file_symbols runs standalone without core module."""
        with tempfile.TemporaryDirectory() as td:
            ts_file = os.path.join(td, "user.ts")
            with open(ts_file, "w", encoding="utf-8") as f:
                f.write("export class UserProfile { id: string; }\n")
            defs_ts, refs_ts = extract_file_symbols(ts_file)
            self.assertIn("UserProfile", defs_ts)

            py_file = os.path.join(td, "model.py")
            with open(py_file, "w", encoding="utf-8") as f:
                f.write("class Account:\n    def get_id(self):\n        pass\n")
            defs_py, refs_py = extract_file_symbols(py_file)
            self.assertIn("Account", defs_py)
            self.assertIn("get_id", defs_py)

    def test_find_ast_grep_standalone(self):
        """Verify find_ast_grep can be invoked without core.capabilities."""
        result = find_ast_grep()
        self.assertTrue(result is None or isinstance(result, str))

    def test_security_auditor_standalone(self):
        """Verify SecurityAuditor runs and identifies vulnerabilities without core dependencies."""
        with tempfile.TemporaryDirectory() as td:
            vuln_file = os.path.join(td, "leak.py")
            with open(vuln_file, "w", encoding="utf-8") as f:
                f.write("import os\nos.system('echo hi')\n")
            auditor = SecurityAuditor(td)
            active, _ = auditor.audit_directory()
            self.assertTrue(len(active) >= 1)
            cats = [item["category"] for item in active]
            self.assertTrue(any("INJECTION" in c or "AST" in c for c in cats))

    def test_hybrid_audit_bundles_no_false_md_skeleton(self):
        """Verify that markdown files never receive [AST-SKELETONIZED] tag in hybrid mode."""
        with tempfile.TemporaryDirectory() as td:
            with open(os.path.join(td, "package.json"), "w") as f:
                f.write('{"name": "test"}')
            with open(os.path.join(td, "DOCS.md"), "w", encoding="utf-8") as f:
                f.write("# Documentation\nLine 1\nLine 2\n")
            with open(os.path.join(td, "util.py"), "w", encoding="utf-8") as f:
                f.write("def helper():\n    return 42\n")
            out_d = os.path.join(td, "bundles")
            bundles = export_audit_bundles(td, out_dir=out_d, hybrid=True, line_numbers=True)
            self.assertTrue(len(bundles) >= 1)
            for b_path in bundles:
                with open(b_path, "r", encoding="utf-8") as fh:
                    b_content = fh.read()
                # If DOCS.md is in this bundle, ensure its File header is NOT labeled AST-SKELETONIZED
                for line in b_content.splitlines():
                    if "DOCS.md" in line and "File: `" in line:
                        self.assertNotIn("[AST-SKELETONIZED]", line)

    def test_generate_ascii_tree_includes_dot_agents(self):
        """Verify generate_ascii_tree includes .agents directory while ignoring other dotfiles."""
        with tempfile.TemporaryDirectory() as td:
            os.makedirs(os.path.join(td, ".agents"))
            os.makedirs(os.path.join(td, ".git"))
            with open(os.path.join(td, "README.md"), "w") as f:
                f.write("# Hi")
            from digestpack.packer import GitIgnoreFilter
            ignore = GitIgnoreFilter(td, exclude_agent_tooling=False)
            tree = generate_ascii_tree(td, max_depth=2, ignore_filter=ignore)
            tree_text = "\n".join(tree)
            self.assertIn(".agents", tree_text)
            self.assertNotIn(".git", tree_text)

    def test_skeleton_syntax_validity_py_compile(self):
        """TEST-01: Skeleton of try/except and long variables compiles without SyntaxError."""
        import py_compile
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
    def run(self, flag: bool = True):
        x = 100
        return x * 2
'''
        skel = skeletonize_python(code, include_line_numbers=False)
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
        self.assertIn(".cmd", DEFAULT_TEXT_EXTENSIONS)

    def test_bundle_file_inventory_table(self):
        """TEST-05: pack_digest generates Bundle File Inventory table when bundle_name is set."""
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


if __name__ == "__main__":
    unittest.main()
