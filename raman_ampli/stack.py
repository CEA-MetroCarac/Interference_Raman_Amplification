"""
Class representing a stack of layers (ordered).
"""


class Stack(list):
    def __init__(self):
        """
        Empty stack.
        """
        self.layers = []
    