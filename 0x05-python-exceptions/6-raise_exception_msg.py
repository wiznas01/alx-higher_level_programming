#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a NameError with a custom message.

    Args:
    - message (str):custom message to include in the exception

    Raises:
    - NameError: Always raises a NameError with the provided message.

    You are not allowed to import any module.
    """
    raise NameError(message)
