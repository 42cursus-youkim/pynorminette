#!/Users/youkim/Repo/pynorminette/.venv/bin/python
# -*- coding: utf-8 -*-

from sys import argv

from termcolor import cprint

from .tester import run_tests
from .utils import show_result


def main() -> None:
    args = argv[1:]
    if not len(args):
        return cprint("no files specified!", on_color="on_red")

    cprint(f"testing {', '.join(args)}", attrs=["bold"])
    results = run_tests(args)
    show_result(results)


if __name__ == "__main__":
    main()
