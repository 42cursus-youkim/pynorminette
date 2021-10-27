#!/Users/youkim/Repo/pynorminette/.venv/bin/python
# -*- coding: utf-8 -*-

from sys import argv
from pynorminette_package import test, Status

from typing import List
from termcolor import cprint, colored

test_suite: 'dict[str, "list[str]"]' = {
    "black": ["--check", "--line-length", "79"],
    "mypy": [],
    "flake8": [],
}


def main():
    args = argv[1:]
    if not len(args):
        cprint("no files specified!", on_color="on_red")
        exit(1)

    results = [
        test(k, args, flags=v) == Status.OK for k, v in test_suite.items()
    ]
    is_pass = Status(not all(results))
    score = colored(
        f"[{results.count(True)}/{len(results)}] ",
        on_color=["on_green", "on_red"][is_pass],
    )
    print(score, is_pass, sep="")


if __name__ == "__main__":
    main()
