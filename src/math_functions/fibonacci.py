import requests  # noqa: F401


def fibonacci(n: int) -> int:
    """Fibonacci function.

    Args:
        n: The n-th fibonacci number.

    Returns:
        The value of the number.
    """

    def next_number(prev: int, current: int, index: int) -> int:
        if index == n - 1:
            return current
        return next_number(current, current+prev, index+1)

    if n < 1:
        raise ValueError("Fibonacci numbers starts from one!")

    if n < 3:
        return 1

    return next_number(1, 1, 1)
