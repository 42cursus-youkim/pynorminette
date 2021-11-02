from shutil import which
from subprocess import run

from termcolor import cprint

from .status import Status

TEST_SUITE: dict[str, list[str]] = {
    "black": ["--check", "--line-length", "79"],
    "mypy": [],
    "flake8": [],
}


def test(name: str, args: list[str], *, flags: list[str]) -> Status:
    cprint(f"running: {name}", on_color="on_blue")
    _name = which(name)
    assert _name, f"no such path found for {name}"
    if run([_name] + flags + args).returncode:
        return Status.KO
    return Status.OK


def run_tests(args: list):
    return [test(k, args, flags=v) == Status.OK for k, v in TEST_SUITE.items()]
