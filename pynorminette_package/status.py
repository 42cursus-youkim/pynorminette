from enum import IntEnum
from termcolor import colored


class Status(IntEnum):
    OK = 0
    KO = 1

    def __str__(self) -> str:
        return colored(
            ["OK!", "KO!"][self], on_color=["on_green", "on_red"][self]
        )


if __name__ == "__main__":
    print(Status.OK, Status.KO)
    print(Status(False), Status(True))
