"""
Source-Packscanner
Zero-Pip AST code skeletonizer, PageRank repo-mapper & context packager for frontier LLM audits.
"""

from .security import (
    sanitize_text,
    SECRET_PATTERNS,
    SecurityAuditor,
    find_ast_grep,
)
from .scanner import (
    skeletonize_code,
    skeletonize_python,
    SUPPORTED_SKELETON_EXTENSIONS,
    build_repo_map,
    calculate_token_stats,
    print_token_stats_table,
    extract_file_symbols,
)
from .packer import (
    ContextPacker,
    export_audit_bundles,
    add_line_numbers,
    get_dynamic_fence,
    collect_git_diff_files,
    clone_remote_repo,
    render_prompt_template,
)
from .dna import (
    ProjectDNA,
    sequence_project_dna,
    classify_file_to_tier,
    mutate_project_dna,
    CANONICAL_5_TIERS,
    CANONICAL_DEPENDENCY_LAWS,
)

__version__ = "0.0.1"
__all__ = [
    "skeletonize_code",
    "skeletonize_python",
    "SUPPORTED_SKELETON_EXTENSIONS",
    "build_repo_map",
    "calculate_token_stats",
    "print_token_stats_table",
    "extract_file_symbols",
    "ContextPacker",
    "export_audit_bundles",
    "sanitize_text",
    "SECRET_PATTERNS",
    "SecurityAuditor",
    "find_ast_grep",
    "add_line_numbers",
    "get_dynamic_fence",
    "collect_git_diff_files",
    "clone_remote_repo",
    "render_prompt_template",
    "ProjectDNA",
    "sequence_project_dna",
    "classify_file_to_tier",
    "mutate_project_dna",
    "CANONICAL_5_TIERS",
    "CANONICAL_DEPENDENCY_LAWS",
]
