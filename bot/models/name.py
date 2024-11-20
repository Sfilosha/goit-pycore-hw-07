"""
This module defines the Name class, which represents the name field in a contact record.

The module includes:
- `Field` from `.field`: The base class for all field types.

Classes:
- `Name`: A subclass of `Field` that represents a contact's name. It ensures that the
name is not empty.

Usage:
- Import the `Name` class to create and manage the name field in a contact record.

Example:
    Creating a Name instance:
        from module_name import Name

        name = Name("John Doe")
        print(name.value)
"""

from .field import Field

class Name(Field):
    """
    Represents the name field in a contact record.

    Attributes:
    - value (str): The name value.

    Methods:
    - __init__: Initializes the Name instance and ensures the name is not empty.
    """

    def __init__(self, value: str) -> None:
        """
        Initializes the Name instance with a value.

        Args:
        - value (str): The name value.

        Raises:
        - ValueError: If the name is empty.
        """
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)
