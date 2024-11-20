"""
This module provides the main classes and structures for managing contact information.

The module includes the following imports:
- `Field` from `.field`: Represents a generic field in a contact record.
- `Name` from `.name`: Represents the name field in a contact record.
- `Phone` from `.phone`: Represents the phone field in a contact record.
- `Record` from `.record`: Represents a contact record containing multiple fields.
- `AddressBook` from `.address_book`: Represents a collection of contact records.

Classes:
- `Field`: A base class for various types of fields in a contact record.
- `Name`: A class representing a contact's name.
- `Phone`: A class representing a contact's phone number.
- `Record`: A class representing a contact record, which can contain
multiple fields such as name and phone.
- `AddressBook`: A class representing an address book, which contains multiple contact records.

Usage:
- Import the necessary classes into your script to create and manage contact records.
- Use `AddressBook` to store and organize multiple `Record` instances.

Example:
    Creating and using an address book:
        from module_name import AddressBook, Record, Name, Phone

        address_book = AddressBook()
        record = Record(Name("John Doe"), Phone("123-456-7890"))
        address_book.add_record(record)
        print(address_book)

The above example demonstrates creating an address book, adding
a contact record, and printing the address book.
"""
from .field import Field
from .name import Name
from .phone import Phone
from .birthday import Birthday
from .record import Record
from .address_book import AddressBook
