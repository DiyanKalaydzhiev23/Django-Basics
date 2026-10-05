from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_bad_language(value: str) -> None:
    bad_language = ["bad_word1", "bad_word2"]

    for word in bad_language:
        if word in value:
            raise ValidationError("This description contains bad language")


@deconstructible
class BadLanguageValidator:
    BAD_WORDS =  ["bad_word1", "bad_word2"]

    def __init__(self, message: str=None) -> None:
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if not isinstance(value, str):
            raise ValueError("Message must be a string!")

        if not value.strip():
            raise ValueError("Message cannot be empty!")

        self.__message = value

    def __call__(self, value: str) -> None:
        for word in self.BAD_WORDS:
            if word in value:
                raise ValidationError(self.message)
