"""
This module defines a class to represent a point in 2D space.
"""


class Points:
    """Class to represent a point in 2D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
