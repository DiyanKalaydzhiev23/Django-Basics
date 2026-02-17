from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex=r'^[A-Za-z0-9_]+$',
                message='Ensure this value contains only letters, numbers, and underscore.',
            )
        ]
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
