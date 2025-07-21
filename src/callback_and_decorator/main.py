"""
Summary: main.py launch the main() demonstrate callback function and decorator.

Author: Chun-Juei Lai 07/19/2025
"""

import datetime

from utility import callback_func, caller, check_today


def main():
    """Entry point of the program."""
    caller(callback_func)
    today = datetime.datetime.now()
    check_today(today)


if __name__ == "__main__":
    main()
