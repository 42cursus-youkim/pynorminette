from .checker import check

__all__ = ["check"]

try:
    import black
    import flake8
    import mypy
except Exception as e:
    print(e)
