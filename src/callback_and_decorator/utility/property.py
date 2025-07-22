"""
The @property decorator allow developers to modify class property using '.' not '()'.

Author: Chun-Juei Lai
Email: chunjueilai@gmail.com
Date: 07/22/2025
"""


class proj_progress(object):
    """A class allows user access attribute with . using @property."""

    def __init__(self, date):
        """Initialize project progress object with deadline."""
        self._deadline = date

    @property
    def deadline(self):
        """Get current deadline of project."""
        try:
            return self._deadline
        except Exception as e:
            print(f"Exception: {e}")

    @deadline.setter
    def deadline(self, date):
        """Set up new deadline of project."""
        self._deadline = date

    @deadline.deleter
    def deadline(self):
        """Delete self._deadline property."""
        try:
            del self._deadline
        except Exception as e:
            print(f"Exception: {e}")
