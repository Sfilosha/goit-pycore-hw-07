from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value: str):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Phone number must contain exactly 10 digits.")
        self.phone = value
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, number: str):
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        phone = self.find_phone(number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError(f"Phone number {number} not found.")
    
    def edit_phone(self, old_number: str, new_number: str):
        old_phone_number = self.find_phone(old_number)
        if not old_phone_number:
            raise ValueError(f"Phone number {old_number} not found.")
        new_phone_number = Phone(new_number)
        old_phone_number.value = new_phone_number.value
    
    def find_phone(self, number: str):
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def add_birthday(self, date: str):
        self.birthday = Birthday(date)

    def __str__(self):
        return f"{self.name} | phones: {'; '.join(p.value for p in self.phones)} | birthday: {self.birthday}"


class AddressBook(UserDict):

    def add_record(self, contact: Record):
        self.data[contact.name.value] = contact

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for contact in self.data.values():
            if contact.birthday is None:
                continue
            
            birthday = contact.birthday.value
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
            days_until_birthday = (birthday_this_year - today).days

            if 0 <= days_until_birthday <= 7:
                congratulation_date = birthday_this_year
                
                weekday = congratulation_date.weekday()
                if weekday == 5:  # Saturday
                    congratulation_date += timedelta(days=2)
                elif weekday == 6:  # Sunday
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append({
                    "name": contact.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays

# TESTING 
if __name__ == "__main__":
    book = AddressBook()
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday("01.04.2026")
    book.add_record(john_record)
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    print(book.get_upcoming_birthdays())
    john.edit_phone("1234567890", "1112223333")
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")
    book.delete("Jane")
