#!/Users/youkim/Repo/pynorminette/.venv/bin/python
# -*- coding: utf-8 -*-

from sys import argv
from typing import List

from termcolor import colored, cprint

from .status import Status
from .tester import test

TEST_SUITE: 'dict[str, "list[str]"]' = {
    "black": ["--check", "--line-length", "79"],
    "mypy": [],
    "flake8": [],
}


def check(args: List[str]):
    if not len(args):
        return cprint("no files specified!", on_color="on_red")

    cprint(f"testing {', '.join(args)}", attrs=["bold"])
    results = [
        test(k, args, flags=v) == Status.OK for k, v in TEST_SUITE.items()
    ]
    is_pass = Status(not all(results))
    score = colored(
        f"[{results.count(True)}/{len(results)}] ",
        on_color=["on_green", "on_red"][is_pass],
    )
    print(score, is_pass, sep="")


if __name__ == "__main__":
    check(["test_ko.py"])
    check(["test_ok.py"])
