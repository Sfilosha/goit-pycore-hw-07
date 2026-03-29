import logger
from classes import AddressBook, Record

@logger.input_error
def parse_input(user_input):
    if not user_input.strip():
        raise ValueError
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@logger.input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    contact = book.find(name)
    message = "Contact updated."
    if contact is None:
        contact = Record(name)
        book.add_record(contact)
        message = f"Contact '{name}' added."
    if phone:
        contact.add_phone(phone)
    return message

@logger.input_error
def change_contact(args, book: AddressBook):
    name, old_number, new_number = args
    contact = book.find(name)
    if contact:
        contact.edit_phone(old_number, new_number)
        return f"Contact '{name}' updated."
    else: 
        return f"Contact '{name}' not found."
    
@logger.input_error
def remove_phone(args, book: AddressBook):
    name, number = args
    contact = book.find(name)
    if contact:
        contact.remove_phone(number)
        return f"Phone of '{name}' removed."
    else: 
        return f"Phone of '{name}' not found."

@logger.input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)
    if contact:
        phones = "; ".join(p.value for p in contact.phones)
        return f"{name}'s phones: {phones}"
    raise KeyError

def show_all(book: AddressBook):
    if not book.data:
        return "No contacts found."
    result = []
    for i, contact in enumerate(book.data.values(), 1):
        result.append(f"{i} | {contact}")
    return "\n".join(result)

def show_commands():
    text = {
        'Add New User': "add <username> <phone>",
        'Change user phone': "change <username> <new phone>",
        'Check user phone': "phone <username>",
        "See all contacts": "all",
        "Add Birthday": "add-birthday <username> <DD.MM.YYYY>",
        "Check User's Birthday": "show-birthday <username>",
        "Upcoming birthdays (next 7 days)": "birthdays",
        "Remove phone": "remove-phone <username> <phone>"
    }
    print("    List of available commands:")
    for purpose, command in text.items():
        print(f"    > {purpose}: {command}")  

@logger.input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    contact = book.find(name)
    if contact:
        contact.add_birthday(birthday)
        return "Birthday added."
    return "Contact not found."

@logger.input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)
    if contact and contact.birthday:
        return f"{name}'s birthday: {contact.birthday.value.strftime('%d.%m.%Y')}"
    return "Birthday not found."

def birthdays(book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays in the next week."
    print("Upcoming birthdays in next 7 days:")
    return "\n".join(f"{item['name']}: {item['congratulation_date']}" for item in upcoming)

def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(contacts))
        elif command == "remove-phone":
            print(remove_phone(args, contacts))
        elif command == "help":
            show_commands()
        else:
            print("Invalid command. Enter 'help' to see all commands.")

if __name__ == "__main__":
    main()
