"""
This module provide python decorator example.

Python provides a way to wrap function up using callback function characteristic.
The wrap function accept callback function and return a wrapped function.
We can also call that wrap function decorate the callback function turn out to another function.

Chun-Juei Lai 07/21/2025
"""

import datetime

FRISTRUN = "2025-07-21 18:03:23"


def decorator_func(callee):
    """Accept callee function and decorate it with wrap_func and return new function."""

    def wrap_func(*args, **kwargs):
        """Wrap up callee to new function."""
        first_run = datetime.datetime.strptime(FRISTRUN, "%Y-%m-%d %H:%M:%S")
        first_run = first_run.strftime("%A %#I:%M:%S %p, %B %d, %Y")
        print(f"The decorator_func build at {first_run}.")
        callee(*args, **kwargs)
        print("Funciton was wrapped up")

    # The decorator_func accept callee function and return type has to be a function.
    return wrap_func


@decorator_func
def check_today(current):
    """Check today to compare to the first time the code was developed."""
    current = current.strftime("%A %#I:%M:%S %p, %B %d, %Y")
    print(f"Today, we run the function at {current}")
