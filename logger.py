from typing import Callable

def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e) if str(e) else "Give me name and phone please."
        except KeyError as e:
            return str(e) if str(e) else "Contact not found."
        except IndexError:
            return "Username is missing: <command> <username>"
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner