<div align="center">

# 📦 Digestpack

### Zero-Pip Markdown Codebase Packager, Polyglot AST Skeletonizer & Security Sanitizer

<p align="center">
  <b>Pack codebases into 10 structured Markdown bundles (<code>.md</code>), AST skeletons, and security digests.</b><br>
  Bypass the 10-file chat upload limit and eliminate context bleed in Gemini, Claude, and ChatGPT.
</p>

<p align="center">
  <a href="https://github.com/Echo-Scion/digestpack/releases"><img src="https://img.shields.io/badge/version-v0.0.1-blue.svg?style=flat-square" alt="Version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg?style=flat-square" alt="License"></a>
  <a href="#-three-anchored-engines"><img src="https://img.shields.io/badge/core-Python%203.10%2B%20Stdlib-brightgreen.svg?style=flat-square" alt="Core"></a>
  <a href="#-zero-pip-mandate"><img src="https://img.shields.io/badge/dependencies-Zero%20Pip-critical.svg?style=flat-square" alt="Zero-Pip"></a>
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

### ⚖️ Mechanical vs Cognitive Proportionality

Frontier language models (Gemini, Claude, ChatGPT) excel at abstract reasoning, architectural judgment, and algorithmic design. However, forcing them to perform low-level mechanical tasks—such as parsing hundreds of raw files, tracing inter-module imports, calculating symbol PageRank, and sanitizing secrets—burns context window capacity, triggers hallucinated references, and induces attention degradation ("lost in the middle").

Digestpack acts as the deterministic mechanical pre-processor. It performs exact mechanical computations (zero-pip AST parsing, secret scrubbing, static risk detection, cross-bundle routing, and balanced bin-packing) on local hardware before any token enters the model prompt. This division of labor frees cognitive tokens entirely for high-order architectural evaluation and logic verification.

---

## ⚡ The Three Pillars

Digestpack combines three essential developer tools into a single, zero-dependency CLI:

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
  • Universal Project DNA v2      • Polyglot AST skeletonizer     • Pre-flight secret scrubbing
  • 10-bundle Markdown (.md)      • PageRank symbol ranking       • Polyglot static audit radar
  • Upload limit bypass (<=10)    • Line span mapping [Lstart-End]• AST taint & injection checks
  • Subtree gravity bin-packing   • BPE token density analytics   • Trojan Source unicode shield
  • Cross-bundle import router    • Global AST symbol compass     • Deterministic safety audits
  • Prompt-bleed quarantine       • CST fast-path via ast-grep    • Sandbox rule enforcement
```

### 1. 📦 The Packer (`packer.py`)
* **Universal Project DNA v2**:
  - **Monorepo & Polyglot Discovery**: Recursively detects polyglot manifests across root and nested sub-containers (`apps/`, `packages/`, `services/`, `modules/`, etc.) without hardcoded paths.
  - **Universal 5-Tier Architectural Taxonomy**: Classifies application files into standard architectural strata: `contracts` (DTOs, schemas, APIs), `domain` (models, entities, usecases), `services` (clients, network, database), `state` (blocs, controllers, stores), and `presentation` (views, screens, components).
  - **Cross-Bundle Import Router**: Traces intra-project dependencies across standard root anchors (`src/`, `lib/`, `app/`, `packages/`), while filtering noisy generic stems (`index`, `main`, `mod`, `route`).
  - **Polyglot Static Audit Radar**: Inspects code across 10+ languages (`.ts`, `.tsx`, `.dart`, `.rs`, `.go`, `.kt`, `.java`, `.py`) for dangerous execution sinks (`eval`, `exec`, `spawn`, `Process.run`, `Runtime.exec`, `dangerouslySetInnerHTML`) and empty catch blocks (`catch {}`), presenting a prioritized pre-audit radar in Bundle 01.
  - **Global AST Symbol Compass**: Indexes polyglot declarations (Rust `pub fn`/`struct`, Go `func`/`type`, TypeScript/React `export const ... =>`, Dart/Java classes) for instant symbol lookups.
  - **Subtree Bin-Packing Balance**: Uses `balance_into_k_bundles()` to distribute code volume evenly across at most 10 bundles, stamping Bundle 01 with the Project DNA Governance Blueprint, Repo-Map, and Router.
* **Universal 10-Bundle Ceiling**: Uses topological architectural gravity (0–9) and subtree bin-packing to cluster any codebase into at most 10 balanced Markdown files (`.md`). Eliminates file explosion and monolithic spikes to comply with Gemini Web Chat's strict 10-file upload limit.
* **Tier-Isolated Subfolder Output**: Exports bundles directly into `.orion/bundles/{arch,hybrid,full}/` to prevent overwriting between different audit runs.
* **Prompt-Bleed Quarantine**: Neutralizes inner code tags into `\<artifact>` and converts imperative instructions into `[TARGET-DATA: ...]` under the `[AUDITOR SANDBOX RULE]` envelope, preventing frontier models from executing target code directives as system prompts.
* **Smart Fence Scaling**: Automatically scales backtick delimiters (````) to prevent Markdown syntax collapse from nested code blocks.
* **Active Code Curation**: Filters downstream scaffolding templates and boilerplate files by default, reserving token context for active production logic (opt back in with `--include-boilerplate`).
* **Git & Remote Ingestion**: Packs uncommitted diffs (`digestpack diff`), staged PR changes (`digestpack pr`), or remote GitHub URLs directly.
* **Multi-Dialect Support**: Outputs clean Markdown, XML, Claude-XML, or Digest formats (`--format`).

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

## 🚀 Quickstart

Clone and run with zero external dependencies (pure Python standard library):

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
| `digestpack hybrid`<br>`digestpack --tier hybrid` | **Tier 2** | **Hybrid** *(Optimal)* | **~350k–400k** | **100% Full Core Code** for execution engines; AST skeletons for manifests and governance rules. | Production codebases balancing token expenditure and deep algorithmic scrutiny. |
| `digestpack full`<br>`digestpack --tier full` | **Tier 3** | **Micro** | **~500k** | **100% Zero-Truncation Full Code**, including unit test suites, active IDE hooks, and playbooks. | Deep security audits, complete logic verification, and zero-blindspot reviews. |
| `digestpack audit` | — | **Lean Full** | **~300k** | **100% Full Code** excluding tests and reference playbooks. | Standard full-code inspection without test suite overhead. |

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

## 🔗 Ecosystem & Integration

Digestpack is maintained as a standalone utility spun off from and best used alongside:

👉 **[Portable Brainvibing (`.agents`)](https://github.com/Echo-Scion/portable-brainvibing)** — Turnkey Auto-Vibe Coding Brain & Cognitive Runtime for Autonomous AI Agents. Turn probabilistic coding AIs into deterministic, self-verifying software engineers.

---

## 📄 License

MIT © 2026 [Echo Scion](https://github.com/Echo-Scion). Zero external dependencies. Pure Python 3.10+ Standard Library.
