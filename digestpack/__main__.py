"""
packscanner main CLI entrypoint.
Directs subcommands to scanner, security, or the unified context packer.
"""
import sys
from .packer import main as packer_main
from .scanner import main as scanner_main
from .security import main as security_main


def main() -> None:
    # Subcommands specifically belonging to scanner or security
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd in ("targets", "map", "repomap", "tokens"):
            scanner_main()
            return
        if cmd in ("scan-security", "security-scan"):
            sys.argv.pop(1)
            security_main()
            return

    # Everything else routes to the full-featured packer CLI
    # (audit, hybrid, architecture, pr, diff, security, stats, URLs, budgets, custom templates)
    packer_main()


if __name__ == "__main__":
    main()
