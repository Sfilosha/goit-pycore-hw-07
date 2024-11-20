"""
This module provides classes for managing contact records, including names and phone numbers.

Classes:
- Name: Represents a contact's name.
- Phone: Represents a contact's phone number.
- Record: Represents a contact record with a name and a list of phone numbers.
"""

from typing import List, Optional

from .name import Name
from .phone import Phone
from .birthday import Birthday

class Record:
    """
    Represents a contact record with a name and a list of phone numbers.

    Attributes:
    - name (Name): The contact's name.
    - phones (List[Phone]): A list of the contact's phone numbers.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a new Record instance with a name.

        Args:
        - name (str): The name of the contact.
        """
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.birthday = None

    def add_phone(self, phone_number: str) -> None:
        """
        Adds a phone number to the contact's list of phone numbers.

        Args:
        - phone_number (str): The phone number to add.
        """
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number: str) -> None:
        """
        Removes a phone number from the contact's list of phone numbers.

        Args:
        - phone_number (str): The phone number to remove.
        """
        self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, old_phone_number: str, new_phone_number: str) -> None:
        """
        Replaces an old phone number with a new phone number in the contact's list.

        Args:
        - old_phone_number (str): The phone number to replace.
        - new_phone_number (str): The new phone number to add.
        """

        self.add_phone(new_phone_number)
        self.remove_phone(old_phone_number)

    def find_phone(self, phone_number: str) -> Optional[Phone]:
        """
        Finds and returns a phone number from the contact's list.

        Args:
        - phone_number (str): The phone number to find.

        Returns:
        - Phone or None: The Phone instance if found, otherwise None.
        """
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_birthday(self, birthday: str) -> None:
        """
        Adds a birthday to the contact record. Raises an exception if the birthday is invalid.

        Args:
        - birthday (str): The birthday to add.
        """
        if self.birthday is None:
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("Birthday is already set")

    def show_birthday(self) -> str:
        """
        Returns a string representation of the contact's birthday.

        Returns:
        - str: A string describing the contact's birthday.
        """
        if self.birthday is None:
            return "No birthday set"
        return f"{self.name.value}'s birthday is on {self.birthday.value.strftime('%d.%m.%Y')}"

    def __str__(self) -> str:
        """
        Returns a string representation of the contact record.

        Returns:
        - str: A string describing the contact's name and phone numbers.
        """
        phones_str = '; '.join(str(p) for p in self.phones)
        if not phones_str:
            phones_str = "----------"

        if self.birthday:
            birthday_str = self.birthday.value.strftime("%d.%m.%Y")
        else:
            birthday_str = "----------"

        return f"Contact name: {self.name.value}, birthday: {birthday_str}, phones: {phones_str}"
