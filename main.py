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
- List from typing: Used for type annotations.
- handlers from bot.cli: Contains functions to handle various contact management commands.
- AddressBook from bot.models: Represents a collection of contact records.
- parse_input from bot.cli.parse_input: Parses user input into commands and arguments.

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

if __name__ == "__main__":
    main()

The above block ensures that the main function runs only when the module is executed
as a script, not when it is imported as a module.
"""

from typing import List

from bot.cli import handlers
from bot.models import AddressBook
from bot.cli.parse_input import parse_input

def main() -> None:
    """
    Runs the assistant bot for managing contacts.

    The function continuously prompts the user for commands and processes them accordingly:
    - 'close' or 'exit' to exit the program
    - 'hello' to greet the user
    - 'add' to add a contact
    - 'change' to update a contact
    - 'phone' to display a contact's phone number
    - 'all' to display all contacts

    Uses handlers from the 'handlers' module for contact management.

    Returns:
    None
    """
    address_book = AddressBook()

    print("Welcome to the assistant bot!")

    while True:
        user_input: str = input("Enter a command: ")

        if not user_input:
            continue

        command: str
        args: List[str]
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(handlers.add_contact(args, address_book))

        elif command == "change":
            print(handlers.change_contact(args, address_book))

        elif command == "phone":
            print(handlers.show_phone(args, address_book))

        elif command == "all":
            print(handlers.show_all(address_book))

        elif command == "add-birthday":
            print(handlers.add_birthday(args, address_book))

        elif command == "show-birthday":
            print(handlers.show_birthday(args, address_book))

        elif command == "birthdays":
            print(handlers.birthdays(address_book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
