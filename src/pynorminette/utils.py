from termcolor import colored

from .status import Status


def show_result(results):
    is_pass = Status(not all(results))
    score = colored(
        f"[{results.count(True)}/{len(results)}] ",
        on_color=["on_green", "on_red"][is_pass],
    )
    print(score, is_pass, sep="")
