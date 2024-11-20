"""
Module provides a decorator to handle common input errors in functions processing user input.

The `input_error` decorator manages errors such as missing arguments,
invalid values, and missing keys.
"""

from typing import Callable, Any

def input_error(func: Callable[..., str]) -> Callable[..., str]:
    """
    Decorator to handle input errors in functions that process user input.

    Args:
        func (Callable[..., str]): The function to decorate.

    Returns:
        Callable[..., str]: A decorated function that handles input errors.
    """
    def wrapper(*args: Any, **kwargs: Any) -> str:
        try:
            return func(*args, **kwargs)
        except ValueError as exc:
            return str(exc) if str(exc) else "Give me name and phone, please."
        except KeyError as exc:
            return str(exc) if str(exc) else "Contact not found."
        except IndexError as exc:
            return str(exc) if str(exc) else "Give me name, please."

    return wrapper
