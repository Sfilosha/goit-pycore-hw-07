"""
This module provides various command handlers and utility functions for the assistant bot.

The module includes the following imports:
- `add_contact`, `change_contact`, `show_phone`, `show_all`
from `.handlers`: Functions for managing contact records.
- `input_error` from `.input_error`: A custom exception class for handling input-related errors.
- `parse_input` from `.parse_input`: A function for parsing user input into commands and arguments.

Functions:
- `add_contact`: Adds a new contact to the address book.
- `change_contact`: Updates an existing contact in the address book.
- `show_phone`: Displays the phone number of a specified contact.
- `show_all`: Displays all contacts in the address book.
- `input_error`: Handles input-related errors by raising a custom exception.
- `parse_input`: Parses the user's input into a command and a list of arguments.

Example:
    Using the functions from this module to manage contacts:
        $ python -m bot.cli
    Interact with the bot using the supported commands to add, change,
    view phone numbers, or display all contacts.

Usage:
    Import the necessary functions into your script to handle user commands for managing contacts.
"""
from .handlers import add_contact, change_contact, show_phone, show_all
from .input_error import input_error
from .parse_input import parse_input
