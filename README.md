<div align="center">

# 📦 Digestpack

### Zero-Pip Markdown Codebase Packager, Polyglot AST Skeletonizer & Security Sanitizer

<p align="center">
  <b>AI agent tool to pack codebases into 10 structured Markdown bundles (<code>.md</code>), AST skeletons, and security digests.</b>

</p>

<p align="center">
  <a href="https://github.com/Echo-Scion/digestpack/releases"><img src="https://img.shields.io/badge/version-v0.0.1-blue.svg?style=flat-square" alt="Version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg?style=flat-square" alt="License"></a>
  <a href="#-three-anchored-engines"><img src="https://img.shields.io/badge/core-Python%203.10%2B%20Stdlib-brightgreen.svg?style=flat-square" alt="Core"></a>
  <a href="#-zero-pip-mandate"><img src="https://img.shields.io/badge/dependencies-Zero%20Pip-critical.svg?style=flat-square" alt="Zero-Pip"></a>
  <a href="#-quickstart"><img src="https://img.shields.io/badge/tests-47%20passed-brightgreen.svg?style=flat-square" alt="Tests"></a>
  <a href="https://github.com/Echo-Scion"><img src="https://img.shields.io/badge/author-Echo--Scion-purple.svg?style=flat-square" alt="Author"></a>
</p>

<p align="center">
  <a href="#-the-three-pillars"><b>The 3 Pillars</b></a> •
  <a href="#-progressive-acceleration-architecture-dual-engine"><b>Dual-Engine</b></a> •
  <a href="#-quickstart"><b>Quickstart</b></a> •
  <a href="#-3-audit-modes"><b>Audit Modes</b></a> •
  <a href="#-scanner--security-commands"><b>Scanner & Security</b></a> •
  <a href="#-ecosystem--integration"><b>Ecosystem</b></a> •
  <a href="LICENSE"><b>License</b></a>
</p>

```bash
pip install .   # or run directly: python -m digestpack audit
```

</div>

---


## 🔗 Portable Brainvibing (`.agents`) Synergy

Digestpack serves as the mechanical packaging backbone of the [Portable Brainvibing (`.agents`)](https://github.com/Echo-Scion/portable-brainvibing) ecosystem:
* **Native Orion Pack**: Inside any `.agents`-enabled repository, Digestpack powers `python .agents/scripts/orion.py pack`.
* **Project DNA Contract**: Ingests `.agents/.dna.json` to cluster source files across the 5-Tier Canonical Strata (`contracts`, `domain`, `services`, `state`, `presentation`).
* **Tier 0 Pillar Locking**: Locks context pillars (`context/00_Strategy/BLUEPRINT.md`, etc.) and root manifests into Bundle 01.
* **Standalone Agent Tool**: Operates independently with zero pip dependencies on any machine running Python 3.10+ without requiring `.agents` installation, ready to be driven directly by AI coding agents (Antigravity CLI, Claude Code, Codex CLI, Cursor) or CLI subshells.

---

### ⚖️ Mechanical vs Cognitive Proportionality

Frontier language models (Gemini, Claude, ChatGPT) excel at abstract reasoning, architectural judgment, and algorithmic design. However, forcing them to perform low-level mechanical tasks—such as parsing hundreds of raw files, tracing inter-module imports, calculating symbol PageRank, and sanitizing secrets—burns context window capacity, triggers hallucinated references, and induces attention degradation ("lost in the middle").

Digestpack acts as the deterministic mechanical pre-processor. It performs exact mechanical computations (zero-pip AST parsing, secret scrubbing, static risk detection, cross-bundle routing, and balanced bin-packing) on local hardware before any token enters the model prompt. This division of labor frees cognitive tokens entirely for high-order architectural evaluation and logic verification.

---

## ⚡ The Three Pillars

Digestpack combines three developer tools into a single, zero-dependency CLI:

```
                      ┌────────────────────────────────────────┐
                      │             DIGESTPACK                │
                      │       Zero-Pip Python Core             │
                      └──────────────────┬─────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         │                               │                               │
         ▼                               ▼                               ▼
  📦 THE PACKER                   🔍 THE SCANNER                  🛡️ THE SECURITY ENGINE
  • Universal Project DNA         • Polyglot AST skeletonizer     • Pre-flight secret scrubbing
  • 10-bundle Markdown (.md)      • PageRank symbol ranking       • Polyglot static audit radar
  • Upload limit bypass (<=10)    • Line span mapping [Lstart-End]• AST taint & injection checks
  • Graph topology bin-packing    • BPE token density analytics   • Trojan Source unicode shield
  • Cross-bundle import router    • Global AST symbol compass     • Deterministic safety audits
  • Prompt-in-data quarantine     • CST fast-path via ast-grep    • Sandbox rule enforcement
```

### 1. 📦 The Packer (`packer.py`)
* **10-Bundle Ceiling**: Clusters any codebase into at most 10 balanced Markdown bundles (`.md`) across 3 audit tiers (`arch/`, `hybrid/`, `full/`), fitting upload limits in Gemini Web, Claude Projects, and ChatGPT.
* **Graph Topology Clustering**: Groups files using PageRank architectural centrality and AST import cohesion, preserving multi-module relationships and native sub-packages without arbitrary bucket collapses.
* **Polyglot Static Audit Radar**: Pre-computes dangerous execution sinks (`exec`, `spawn`, `MethodChannel`) and broad catch blocks into Bundle 01 for zero-turn risk discovery.
* **Interactive 4-Turn Playbook**: Automatically generates `00_GEMINI_WEB_AUDIT_PROMPT.txt` orchestrating phased multi-turn reviews with automated test verification.
* **Prompt-in-Data Shield**: Neutralizes prompt tags and escapes `<artifact>` delimiters across all lines (including code fences) to prevent context hijacking.
* **Active Code Curation**: Filters downstream scaffolding templates and boilerplate files by default (opt back in with `--include-boilerplate`).
* **Git & Remote Ingestion**: Packs uncommitted working trees (`digestpack diff`), staged PR changes (`digestpack pr`), or remote GitHub repositories directly.
* **Multi-Dialect Output**: Supports clean Markdown, XML, Claude-XML, and Digest formats (`--format`).

### 2. 🔍 The Scanner (`scanner.py`)
* **Polyglot AST Skeletonizer**: Collapses function bodies while preserving signatures, types, and docstrings across 10+ languages (cuts token weight **60%–85%**).
* **PageRank Repo-Mapper**: Ranks symbols by architectural centrality to fit large codebases into strict token budgets.
* **Line Span Mapping**: Generates precise `[Lstart-Lend]` line maps for zero-sequential-paging agent navigation.
* **Token Analytics**: Exact BPE token counts and density breakdown by extension (`digestpack stats`).

### 3. 🛡️ The Security Engine (`security.py`)
* **Secret Scrubbing**: Automatically redacts AWS, Stripe, GitHub, JWT, and private keys before code leaves your machine.
* **AST Taint Scanner**: Flags `eval()`, `exec()`, `shell=True`, SQL injection, and path traversal in Python AST.
* **Trojan Source Shield**: Intercepts invisible Unicode characters and Bidi overrides (`\u202a`–`\u202e`) used in supply-chain attacks.

---

## ⚡ Progressive Acceleration Architecture (Dual-Engine)

Digestpack is built on a two-tier execution model that balances **zero-dependency portability** with **native binary performance**:

```
┌────────────────────────────────────────────────────────┐
│                   Digestpack Engine                   │
├──────────────────────────┬─────────────────────────────┤
│ Native Python 3 (Base)   │ Cargo/Rust Binaries (Turbo) │
├──────────────────────────┼─────────────────────────────┤
│ • Zero-pip stdlib core   │ • ast-grep (sg)             │
│ • Python AST parser      │   - Polyglot CST parsing    │
│ • PageRank power-iter    │   - High-speed AST security │
│ • Regex heuristic fallbk │ • rtk (Rust Token Killer)   │
│ • Secret sanitization    │   - CLI terminal proxy      │
└──────────────────────────┴─────────────────────────────┘
```

* **Native Python 3.10+ Base (Zero-Pip)**: Runs out of the box on any machine with Python 3.10+. Zero external packages (`dependencies = []`), zero build toolchains, and zero PyPI downloads.
* **Cargo / Rust Turbo Acceleration (Auto-Detected)**:
  - **`ast-grep` (`sg`)**: If detected in `PATH`, `~/.cargo/bin`, or `~/.bun/bin`, Digestpack automatically delegates polyglot symbol extraction and AST vulnerability queries to `sg` for streaming, sub-second Concrete Syntax Tree (CST) parsing across Dart, TypeScript, Rust, Go, Java, and Kotlin.
  - **`rtk` (Rust Token Killer)**: Automatically proxies shell invocations to slash token consumption by 60%–90% during agent workflows.
* **Graceful Degradation**: When native Rust binaries are not installed, Digestpack seamlessly falls back to its built-in Python AST parser and regex heuristic engine without missing a beat or throwing fatal errors.

---

## 🚀 Quickstart for AI Coding Agents

Digestpack operates with zero external pip packages (pure Python 3.10+ standard library). To run standalone without [Portable Brainvibing (`.agents`)](https://github.com/Echo-Scion/portable-brainvibing), AI coding agents or developers can clone and execute directly:

```bash
# Clone the repository
git clone https://github.com/Echo-Scion/digestpack.git
cd digestpack

# Install in editable mode
pip install -e .
```

Or run directly without installation:

```bash
python -m digestpack audit
```

---

## 🎯 Packaging & Multi-Tier Audit Modes

Digestpack enforces a **strict ceiling of at most 10 Markdown bundles (`.md`)** across all tiers, matching the 10-file attachment limit in Gemini Web Chat, Claude Projects, and ChatGPT. Each tier writes to an isolated directory under `.orion/bundles/` to prevent collisions.

| Command / Flag | Tier | Depth | Token Footprint | What AI Inspects | Optimal Use Case |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `digestpack arch`<br>`digestpack --tier arch` | **Tier 1** | **Macro** | **~60k–100k** | **Pure AST Skeletons** (`class`, `def`, method signatures, types, docstrings). | Architecture reviews, cross-package dependency routing, and multi-million line codebases. |
| `digestpack hybrid`<br>`digestpack --tier hybrid` | **Tier 2** | **Hybrid** *(Optimal)* | **~100k–400k** | **100% Full Core Code** for execution engines, test suites (`test/`, `src/tests/`), and `.arb` localization; AST skeletons for manifests and governance rules; marketing copy pruned. | Production codebases balancing token expenditure and deep algorithmic scrutiny. |
| `digestpack full`<br>`digestpack --tier full` | **Tier 3** | **Micro** | **~500k–800k** | **100% Zero-Truncation Full Code**, including unit test suites, active IDE hooks, and playbooks. | Deep security audits, complete logic verification, and zero-blindspot reviews. |
| `digestpack audit` | — | **Lean Full** | **~250k–350k** | **100% Full Code** excluding tests and reference playbooks. | Standard full-code inspection without test suite overhead. |

### Directory Structure & Upload Isolation

Output bundles are saved into three clean tier subfolders:

```
.orion/bundles/
├── arch/      # Tier 1: 10 Macro AST skeleton bundles (~5k-35k tokens each)
├── hybrid/    # Tier 2: 10 Balanced core code + signature bundles (~25k-75k tokens each)
└── full/      # Tier 3: 10 Zero-truncation complete codebase bundles (~35k-75k tokens each)
```

Drag and drop all 10 `.md` files from any tier directory directly into your model prompt in a single upload.

### Curated vs Full Boilerplate Options

In `full` mode, Digestpack curates active source code and test suites while excluding downstream scaffolding templates and canon components to prevent context bloat:

```bash
# Default: Packs active source code, tests, and skills (omits inert downstream boilerplate)
digestpack full

# Include all downstream scaffolding templates and canon sample files
digestpack full --include-boilerplate
```

---

## 🔍 Scanner & Security Commands

| Command | Engine | Description |
| :--- | :--- | :--- |
| `digestpack security` | 🛡️ Security | Scans codebase AST for injection risks, scrubs secrets, and packs a dedicated `security_audit.md`. |
| `digestpack stats` | 🔍 Scanner | Generates a token density matrix breakdown by file extension and directory weight. |
| `digestpack pr` | 📦 Packer | Extracts staged Git changes and packages a targeted diff digest for PR code reviews. |
| `digestpack diff` | 📦 Packer | Packs all uncommitted working tree modifications. |
| `digestpack <github-url>` | 🌐 Ingestion | Clones and skeletonizes a remote GitHub repository directly into a Claude/Gemini-ready XML bundle. |

---

## 🏛️ Languages Supported

- **Native AST Deep Parsing**: Python 3 (full AST inspection, type annotations, taint tracing, and decorator resolution).
- **Polyglot Structural Skeletonization**: TypeScript / JavaScript, Dart / Flutter, Rust, Go, Kotlin, Java, C / C++, Swift, and C#.

---

## 👥 Contributors

* [@Echo-Scion](https://github.com/Echo-Scion) — Core maintainer & architecture
* **Google Gemini** (AI Pair Programmer) — Architecture drafting, test generation & refactoring

---

## 📄 License

MIT © 2026 [Echo Scion](https://github.com/Echo-Scion). Zero external dependencies. Pure Python 3.10+ Standard Library.
