"""
Summary: main.py launch the main() demonstrate callback function and decorator.

Author: Chun-Juei Lai 07/19/2025
"""

import datetime

from .utility import callback_func, caller, check_today, proj_progress


def main():
    """Entry point of the program."""
    # Demonstrate callback function.
    caller(callback_func)
    # Demonstrate decorator.
    today = datetime.datetime.now()
    check_today(today)
    # Demonstrate @property.
    new_proj = proj_progress(date=90)
    print(f"new_proj deadline is {new_proj.deadline} days")
    new_proj.deadline = 120
    print(f"Updated new_proj deadline is {new_proj.deadline} days")
    del new_proj.deadline
    print(f"Let's find out if deadline still exist: {new_proj.deadline}")


if __name__ == "__main__":
    main()
