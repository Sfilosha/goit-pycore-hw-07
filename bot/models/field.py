"""
This module defines the Field class, which represents a simple data field.

Classes:
- Field: A class that represents a field with a value.

Usage:
- The Field class can be used to encapsulate a single value and provide
a string representation of it.
"""
from typing import Any
class Field:
    """
    A class representing a simple data field with a value.

    Attributes:
        value (Any): The value stored in the field.

    Methods:
        __str__() -> str:
            Returns a string representation of the field's value.
    """

    def __init__(self, value: Any) -> None:
        """
        Initializes a new Field instance with a given value.

        Args:
            value (Any): The value to be stored in the field.
        """
        self.value = value

    def __str__(self) -> str:
        """
        Returns a string representation of the field's value.

        Returns:
            str: The string representation of the field's value.
        """
        return str(self.value)
