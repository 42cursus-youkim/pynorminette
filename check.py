#!/Users/youkim/Repo/pynorminette/.venv/bin/python
# -*- coding: utf-8 -*-

from sys import argv
from pynorminette_package import test, Status

from typing import List
from termcolor import cprint

test_suite: 'dict[str, "list[str]"]' = {
    "mypy": [],
    "black": ["--check"],
    "flake8": [],
    # "pylint": ['-q',  "--output-format=colorized"],
}


def main():
    args = argv[1:]
    results = [
        test(k, args, flags=v) == Status.OK for k, v in test_suite.items()
    ]
    print(Status(not all(results)))


if __name__ == "__main__":
    if len(argv) <= 1:
        cprint("no files specified!", on_color="on_red")
        exit(1)

    main()
