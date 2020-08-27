#!/usr/bin/python3
"""Module My list."""


class MyList(list):
    """Class that inherits from list."""

    def print_sorted(self):
        """Print the list in sorted order."""
        print(sorted(self))
