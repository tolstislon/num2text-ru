from typing import Any


class Num2TextException(Exception):
    """Base class for exceptions"""


class InvalidNumberException(Num2TextException):

    def __init__(self, value: Any) -> None:
        super().__init__(f"Invalid number '{type(value)}'. Must be a number: int, float, Decimal")


class InvalidTypeException(Num2TextException):

    def __init__(self, value1: Any, value2: Any) -> None:
        super().__init__(f"Invalid type '{type(value1).__name__}' and '{type(value2).__name__}'")


class LargeNumberException(Num2TextException):

    def __init__(self):
        super().__init__("Such a large number is not supported")


class NumberTooBigException(Num2TextException):

    def __init__(self):
        super().__init__("The number is too big")


class ValueIsNotANumber(Num2TextException):

    def __init__(self, value: Any) -> None:
        super().__init__(f'Value "{value}" is not a number')
