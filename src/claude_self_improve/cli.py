"""CLI entry point for claude-self-improve."""

import argparse
import sys

from claude_self_improve import __version__
from claude_self_improve.init_command import run_init
from claude_self_improve.link_command import run_link


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="claude-self-improve",
        description=(
            "Scaffold a .claude/ governance framework for "
            "self-improving AI agents."
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    subparsers = parser.add_subparsers(dest="command")

    # init subcommand
    init_parser = subparsers.add_parser(
        "init",
        help="Initialize .claude/ governance framework in current directory",
    )
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing .claude/ directory",
    )
    init_parser.add_argument(
        "--target",
        type=str,
        default=".",
        help="Target directory (default: current directory)",
    )

    # link subcommand
    link_parser = subparsers.add_parser(
        "link",
        help="Create memory symlink for Claude Code",
    )
    link_parser.add_argument(
        "--target",
        type=str,
        default=".",
        help="Project directory containing .claude/ (default: current directory)",
    )

    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 1

    if args.command == "init":
        return run_init(target=args.target, force=args.force)

    if args.command == "link":
        return run_link(target=args.target)

    return 0
