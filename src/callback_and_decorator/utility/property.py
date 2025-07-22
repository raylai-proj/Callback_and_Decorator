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
