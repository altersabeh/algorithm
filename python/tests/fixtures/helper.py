from typing import TypeVar

T = TypeVar("T")


def error_message(actual: T, expected: T) -> str:
    return f"Expected: {expected}, but got: {actual}"
