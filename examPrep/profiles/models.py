from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from profiles.validators import AlphaNumericUnderscoreValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericUnderscoreValidator(),
        ]
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
        ]
    )