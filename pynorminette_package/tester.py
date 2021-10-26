from .status import Status

from shutil import which
from subprocess import CalledProcessError, check_output, run, STDOUT
from typing import List
from termcolor import cprint


def test(name: str, args: List[str], *, flags: List[str] = []) -> Status:
    cprint(f"running: {name}", on_color="on_blue")
    _name = which(name)
    assert _name, f"no such path found for {name}"

    if run([_name] + flags + args).returncode:
        return Status.KO
    return Status.OK
