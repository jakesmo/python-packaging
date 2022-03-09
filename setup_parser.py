import argparse
import sys

class CustomHelpFormatter(argparse.HelpFormatter):
    """Custom help formatter to remove usage/prefix"""

    def add_usage(self, usage, actions, groups):
        return super(CustomHelpFormatter, self).add_usage(usage, actions, groups, "")


def parse_test_arg():
    """Parses known arguments and passes the remaining arguments back to the program."""
    parser = argparse.ArgumentParser(
        "", usage="", description="", add_help=False, formatter_class=CustomHelpFormatter
    )
    parser._optionals.title = "PACKAGE setup options"
    parser.add_argument(
        "--test",
        action="store_true",
        help="Used when testing a build to prevent inadvertent overwriting \
            of a versioned artifacts.",
    )
    parser.add_argument(
        "-h",
        "--help",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    custom_args, standard_args = parser.parse_known_args()

    if custom_args.help:
        parser.print_help()

    # normalize setup arguments by filter custom arguments from sys.argv
    sys.argv = [sys.argv[0]] + (["-h"] if custom_args.help else []) + standard_args

    return custom_args.test
