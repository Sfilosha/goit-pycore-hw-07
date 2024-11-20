"""
Module providing functions for parsing user input.

Functions:
- parse_input(user_input: str) -> tuple: Parses user input into a command and its arguments.
"""

def parse_input(user_input: str) -> tuple:
    """
    Parses user input into a command and its arguments.

    Args:
    user_input (str): The input string from the user containing the command and optional arguments.

    Returns:
    tuple: A tuple containing the command (str) and its arguments (list of str).

    Example:
    >>> parse_input("Search file.txt")
    ('search', ['file.txt'])
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

if __name__ == "__main__":
    print(parse_input('hello'))  # ('hello', [])
    print(parse_input('add Mary 1234567'))  # ('add', ['Mary', '1234567'])
    print(parse_input('change Mary 7654321'))  # ('change', ['Mary', '7654321'])
    print(parse_input('phone Mary'))  # ('phone', ['Mary'])
    print(parse_input('all'))  # ('all', [])
    print(parse_input('exit'))  # ('exit', [])
    print(parse_input('invalid_command'))  # ('invalid_command', [])
