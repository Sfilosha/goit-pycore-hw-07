"""
This module provides the main function to run an assistant bot for managing contacts.

The assistant bot supports the following commands:
- 'close' or 'exit': Exit the program.
- 'hello': Greet the user.
- 'add': Add a new contact.
- 'change': Update an existing contact.
- 'phone': Display a contact's phone number.
- 'all': Display all contacts.

Imports:
- `handlers` from `.cli`: Contains functions to handle various contact management commands.
- `AddressBook` from `.models`: Represents a collection of contact records.
- `parse_input` from `.cli.parse_input`: Parses user input into commands and arguments.

Functions:
- main: The entry point of the assistant bot, which continuously prompts the user
  for commands and processes them accordingly.

Usage:
- Run the module as a script to start the assistant bot.
- The bot will prompt the user for commands and manage the contact records in the AddressBook.

Example:
    Run the script:
        $ python module_name.py
    Interact with the bot using the supported commands.

Main Function:
- main: Initializes the AddressBook and enters an infinite loop to handle user commands
  until 'close' or 'exit' is entered.
"""
from .cli import handlers
from .models import AddressBook
from .cli.parse_input import parse_input
