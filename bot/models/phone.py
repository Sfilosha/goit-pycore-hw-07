"""
This module defines the Phone class, which represents a phone number.

Classes:
- Phone: A class that represents a phone number with validation.

Usage:
- The Phone class inherits from Field and validates that the phone number is exactly 10 digits long.
"""
import re
from .field import Field

class Phone(Field):
    """
    A class representing a phone number with validation.

    Inherits:
        Field: The base class representing a simple data field.

    Attributes:
        value (str): The phone number stored in the field.

    Methods:
        __init__(value: str) -> None:
            Initializes a new Phone instance with validation.
    """

    def __init__(self, value: str) -> None:
        """
        Initializes a new Phone instance with a given value, ensuring it is a valid phone number.

        Args:
            value (str): The phone number to be stored in the field.

        Raises:
            ValueError: If the phone number does not consist of exactly 10 digits.
        """
        if not re.fullmatch(r'\d{10}', value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)
        
