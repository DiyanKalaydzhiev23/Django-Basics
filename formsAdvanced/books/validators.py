from collections.abc import Callable
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def range_validator(value: Decimal):
    if not 0 <= value <= 1000:
        raise ValidationError("The value must be in the range 0 - 1000")


def range_validator2(min_value: int, max_value: int) -> Callable:
    def validator(value) -> None:
        if not min_value <= value <= max_value:
            raise ValidationError(f"The value must be in the range {min_value} - {max_value}")

    return validator


@deconstructible
class RangeValidator:
    def __init__(self, min_value: int, max_value: int, message: str="") -> None:
        self.min_value = min_value
        self.max_value = max_value
        self.message = message

    @property
    def min_value(self):
        return self.__min_value

    @min_value.setter
    def min_value(self, value):
        if value < 0:
            raise ValueError("Min value cannot be null")

        self.__min_value = value

    def __call__(self, value: Decimal) -> None:
        if not self.min_value <= value <= self.max_value:
            raise ValidationError(self.message)


