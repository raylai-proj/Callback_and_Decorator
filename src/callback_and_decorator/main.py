"""
Summary: main.py launch the main() demonstrate callback function and decorator.

Author: Chun-Juei Lai 07/19/2025
"""

from utility import callback_func, caller


def main():
    """Entry point of the program."""
    caller(callback_func)


if __name__ == "__main__":
    main()
