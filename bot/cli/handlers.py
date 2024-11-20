"""
This module provides functions to manage contacts using AddressBook, Record,
Name, and Phone classes.

Functions:
- add_contact(args: List[str], address_book: AddressBook) -> str:
  Adds a new contact with the given name and phone number to the address book.

- change_contact(args: List[str], address_book: AddressBook) -> str:
  Updates the phone number of an existing contact in the address book.

- show_phone(args: List[str], address_book: AddressBook) -> str:
  Retrieves the phone number of a contact from the address book.

- show_all(address_book: AddressBook) -> str:
  Retrieves all contacts stored in the address book.

- add_birthday(args: List[str], address_book: AddressBook) -> str:
  Adds a birthday to a contact or creates a new contact with the birthday.

- show_birthday(args: List[str], address_book: AddressBook) -> str:
  Retrieves the birthday of a contact from the address book.

- birthdays(address_book: AddressBook) -> str:
  Retrieves a list of upcoming birthdays from the address book.

Usage:
This module can be imported and used in other Python scripts to manage a collection
of contacts. Each function handles specific operations related to adding, updating,
and retrieving contact information.
"""

from typing import List
from bot.models import AddressBook, Record
from bot.cli.input_error import input_error

@input_error
def add_contact(args: List[str], address_book: AddressBook) -> str:
    """
    Add a new contact with the given name and phone number to the address book.

    Parameters:
    args (List[str]): List of arguments containing name and phone number.
    address_book (AddressBook): The address book where the contact will be added.

    Returns:
    str: Success or error message indicating whether the contact was added successfully
    or if the phone number already exists for the contact.
    """
    if len(args) < 2:
        return "Insufficient arguments. Usage: add <name> <phone>"

    name_str, phone_str = args

    record = address_book.find(name_str)

    if record:
        if record.find_phone(phone_str):
            return f"Contact {name_str} already has this phone number."
        record.add_phone(phone_str)
        return f"Phone number added to existing contact {name_str}."

    record = Record(name_str)
    record.add_phone(phone_str)
    address_book.add_record(record)
    return "Contact added."

@input_error
def change_contact(args: List[str], address_book: AddressBook) -> str:
    """
    Update the phone number of an existing contact in the address book.

    Parameters:
    args (List[str]): List of arguments containing name, old phone number, and new phone number.
    address_book (AddressBook): The address book where the contact exists.

    Returns:
    str: Success or error message indicating whether the contact was updated
    successfully, or if it was not found, or if the old phone number was not found.
    """
    if len(args) < 3:
        return "Insufficient arguments. Usage: change <name> <old_phone> <new_phone>"

    name_str, old_phone_str, new_phone_str = args
    record = address_book.find(name_str)

    if not record:
        return f"No contact found with name {name_str}."

    if not record.find_phone(old_phone_str):
        return f"No phone number {old_phone_str} found for contact {name_str}."

    record.edit_phone(old_phone_str, new_phone_str)
    return "Contact updated."

@input_error
def show_phone(args: List[str], address_book: AddressBook) -> str:
    """
    Retrieve the phone number(s) of a contact from the address book.

    Parameters:
    args (List[str]): List of arguments containing the name of the contact.
    address_book (AddressBook): The address book where the contact exists.

    Returns:
    str: Phone number(s) of the contact if found, otherwise a message indicating
    the contact was not found.
    """
    if len(args) != 1:
        return "Insufficient arguments. Usage: phone <name>"

    name_str = args[0]
    record = address_book.find(name_str)

    if not record:
        return f"No contact found with name {name_str}."

    return str(record)

@input_error
def show_all(address_book: AddressBook) -> str:
    """
    Retrieve all contacts stored in the address book.

    Parameters:
    address_book (AddressBook): The address book containing contacts.

    Returns:
    str: All contacts in the address book or a message indicating it's empty.
    """
    if not address_book.data:
        return "No contacts."

    return str(address_book)

@input_error
def add_birthday(args: List[str], address_book: AddressBook) -> str:
    """
    Add a birthday to a contact or create a new contact with the birthday.

    Parameters:
    args (List[str]): List of arguments containing name and birthday.
    address_book (AddressBook): The address book where the contact will be added or updated.

    Returns:
    str: Success or error message indicating whether the birthday was added successfully
    or if there were insufficient arguments.
    """
    if len(args) < 2:
        return "Insufficient arguments. Usage: add <name> <birthday>"

    name_str, birthday_str = args

    record = address_book.find(name_str)

    if record:
        record.add_birthday(birthday_str)
        return f"Birthday added to existing contact {name_str}."

    record = Record(name_str)
    record.add_birthday(birthday_str)
    address_book.add_record(record)
    return "Contact with birthday added."

@input_error
def show_birthday(args: List[str], address_book: AddressBook) -> str:
    """
    Retrieve the birthday of a contact from the address book.

    Parameters:
    args (List[str]): List of arguments containing the name of the contact.
    address_book (AddressBook): The address book where the contact exists.

    Returns:
    str: The birthday of the contact if found, otherwise a message indicating
    the contact was not found.
    """
    if len(args) != 1:
        return "Insufficient arguments. Usage: show-birthday <name>"

    name_str = args[0]
    record = address_book.find(name_str)

    if not record:
        return f"No contact found with name {name_str}."

    return record.show_birthday()

@input_error
def birthdays(address_book: AddressBook) -> str:
    """
    Retrieve a list of upcoming birthdays from the address book.

    Parameters:
    address_book (AddressBook): The address book containing contacts.

    Returns:
    str: A list of upcoming birthdays or a message indicating there are no contacts.
    """
    if not address_book.data:
        return "No contacts."

    return address_book.get_upcoming_birthdays()


if __name__ == "__main__":
    print()

    contacts_list = AddressBook()

    # Test show_all
    # Should show all contacts
    print(show_all(contacts_list))
    print()

    # Test add_contact
    print('Test add_contact >>>')
    # Should add contact successfully
    print(add_contact(["John", "123456789"], contacts_list))
    # Should indicate contact already exists
    print(add_contact(["John", "987654321"], contacts_list))
    # Should indicate invalid arguments
    print(add_contact(["John"], contacts_list))
    # Should indicate invalid arguments
    print(add_contact([], contacts_list))
    print()

    # Test change_contact
    print('Test change_contact >>>')
    # Should update contact successfully
    print(change_contact(["John", "987654321"], contacts_list))
    # Indicates that contact already has this phone number
    print(change_contact(["John", "987654321"], contacts_list))
    # Should indicate contact not found
    print(change_contact(["Mary", "456789123"], contacts_list))
    # Should indicate invalid arguments
    print(change_contact(["John"], contacts_list))
    # Should indicate invalid arguments
    print(change_contact([], contacts_list))
    print()

    # Test show_phone
    print('Test show_phone >>>')
    # Should show phone number for John
    print(show_phone(["John"], contacts_list))
    # Should indicate contact not found
    print(show_phone(["Mary"], contacts_list))
    # Should indicate invalid arguments
    print(show_phone(["John", "Mary"], contacts_list))
    # Should indicate invalid arguments
    print(show_phone([], contacts_list))
    print()

    # Test show_all
    # Should show all contacts
    print(show_all(contacts_list))
    print()
