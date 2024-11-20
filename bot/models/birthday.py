"""
This module defines the Birthday class for managing birthday information as part
of a contact management system. The Birthday class extends the Field class to
include birthday-specific validation and formatting.

The Birthday class ensures that:
- The provided date is in the format DD.MM.YYYY.
- The date is not in the future.
- The value is stored as a datetime object.

Usage:
Import the Birthday class and instantiate it with a date string to create a
birthday object. Ensure that the date string adheres to the expected format and
represents a valid date in the past.
"""

from datetime import datetime
from .field import Field

class Birthday(Field):
    """
    Represents a birthday field in a contact management system.

    Inherits from the Field class and provides functionality for validating and
    storing birthday information. The date must be in the format DD.MM.YYYY and
    cannot be a future date.

    Attributes:
    value (datetime): The birthday date stored as a datetime object.

    Parameters:
    value (str): A string representing the birthday date in the format DD.MM.YYYY.

    Raises:
    ValueError: If the date format is incorrect or if the date is in the future.
    """

    def __init__(self, value: str) -> None:
        """
        Initialize a Birthday object with the provided date string.

        Parameters:
        value (str): A string representing the birthday date in the format DD.MM.YYYY.

        Raises:
        ValueError: If the date format is incorrect or if the date is in the future.
        """
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y")
            if birthday_date > datetime.now():
                raise ValueError("Birthday date cannot be in the future")
            self.value = birthday_date
        except ValueError as exc:
            if "unconverted data remains" in str(exc) or "does not match format" in str(exc):
                raise ValueError("Invalid date format. Use DD.MM.YYYY") from exc
            raise
        super().__init__(birthday_date)
