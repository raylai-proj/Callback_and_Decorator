"""
The callback.py setup an example about how callback function works.

Chun-Juei Lai 07/19/2025
"""


def caller(callback):
    """Accept function and calls in it."""
    print(
        "1. Caller accepts function as an argument.\n"
        "2. Caller calls that function in its own function."
    )
    callback()
    print(
        "When these 2 factors satisfied, the function that caller accepts is a callback function.\n"
        "==================================================\n"
    )


def callback_func():
    """Input as an argument of another function."""
    print(
        "\n*\nThis is a callback function which is an argument of another function.\n*\n"
    )
