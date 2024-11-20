"""
This module provides classes for managing a contact address book. It includes:

- Field: A base class for various types of fields such as names and phone numbers.
- Name: A class representing a contact name, which cannot be empty.
- Phone: A class representing a phone number, which must be exactly 10 digits.
- Record: A class for a contact record, containing a name and a list of phone
numbers. It supports adding, removing, editing, and finding phone numbers.
- AddressBook: A class for managing a collection of contact records. It supports
adding, finding, and deleting records by name.

Usage:
    To use these classes, create instances of Record and AddressBook. Add phone
    numbers to records, add records to the address book, and manage the records
    using the provided methods.
"""

from collections import UserDict
import re
from typing import Any, List, Optional

class Field:
    """
    Base class for fields in contact records. This class provides basic functionality
    for fields such as name and phone number.

    Attributes:
        value (Any): The value of the field.
    """

    def __init__(self, value: Any) -> None:
        """
        Initializes the field with a value.

        Args:
            value (Any): The value to initialize the field with.
        """
        self.value = value

    def __str__(self) -> str:
        """
        Returns a string representation of the field's value.

        Returns:
            str: The value of the field as a string.
        """
        return str(self.value)

class Name(Field):
    """
    Represents a contact name. The name cannot be empty.

    Inherits from:
        Field: Base class for fields.

    Attributes:
        value (str): The name of the contact.
    """

    def __init__(self, value: str) -> None:
        """
        Initializes the name with a value. Raises an exception if the name is empty.

        Args:
            value (str): The name to initialize the field with.
        
        Raises:
            ValueError: If the name is empty.
        """
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    """
    Represents a phone number. The phone number must be exactly 10 digits.

    Inherits from:
        Field: Base class for fields.

    Attributes:
        value (str): The phone number.
    """

    def __init__(self, value: str) -> None:
        """
        Initializes the phone number with a value. Raises an exception if the phone number
        is not exactly 10 digits.

        Args:
            value (str): The phone number to initialize the field with.
        
        Raises:
            ValueError: If the phone number is not exactly 10 digits.
        """
        if not re.fullmatch(r'\d{10}', value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

class Record:
    """
    Represents a contact record, which includes a name and a list of phone numbers.

    Attributes:
        name (Name): The name of the contact.
        phones (List[Phone]): A list of phone numbers associated with the contact.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes the record with a contact name and an empty list of phone numbers.

        Args:
            name (str): The name of the contact.
        """
        self.name = Name(name)
        self.phones: List[Phone] = []

    def add_phone(self, phone_number: str) -> None:
        """
        Adds a phone number to the record. Raises an exception if the phone number is invalid.

        Args:
            phone_number (str): The phone number to add.
        
        Raises:
            ValueError: If the phone number is invalid.
        """
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number: str) -> None:
        """
        Removes a phone number from the record.

        Args:
            phone_number (str): The phone number to remove.
        """
        self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, old_phone_number: str, new_phone_number: str) -> None:
        """
        Edits an existing phone number in the record by removing the old number and adding
        the new one.

        Args:
            old_phone_number (str): The phone number to be replaced.
            new_phone_number (str): The new phone number to add.
        
        Raises:
            ValueError: If the new phone number is invalid.
        """
        self.remove_phone(old_phone_number)
        self.add_phone(new_phone_number)

    def find_phone(self, phone_number: str) -> Optional[Phone]:
        """
        Finds a phone number in the record.

        Args:
            phone_number (str): The phone number to find.

        Returns:
            Optional[Phone]: The found phone number or None if not found.
        """
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self) -> str:
        """
        Returns a string representation of the contact record, including the name and phone numbers.

        Returns:
            str: A string representing the contact record.
        """
        phones_str = '; '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    """
    Represents an address book that manages a collection of contact records.

    Inherits from:
        UserDict: A dictionary-like class for managing records.

    Methods:
        add_record(record: Record) -> None:
            Adds a new record to the address book.

        find(name: str) -> Optional[Record]:
            Finds and returns a record by the contact's name.

        delete(name: str) -> None:
            Deletes a record from the address book by the contact's name.
    """

    def add_record(self, record: Record) -> None:
        """
        Adds a new record to the address book.

        Args:
            record (Record): The record to be added.
        """
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        """
        Finds and returns a record by the contact's name.

        Args:
            name (str): The name of the contact to find.

        Returns:
            Optional[Record]: The found record or None if not found.
        """
        return self.data.get(name, None)

    def delete(self, name: str) -> None:
        """
        Deletes a record from the address book by the contact's name.

        Args:
            name (str): The name of the contact to delete.
        """
        if name in self.data:
            del self.data[name]

    def __str__(self) -> str:
        """
        Returns a string representation of all records in the address book.

        Returns:
            str: A string representing all records in the address book.
        """
        return "\n".join(str(record) for record in self.data.values())

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

     # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)
