from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from common.choices import CountryChoice
from travelers.validators import validate_email_domain


class Traveler(models.Model):
    name = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        unique=True,
        validators=[validate_email_domain],
    )
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18)],
    )
    country = models.CharField(
        max_length=10,
        choices=CountryChoice.choices,
    )
    registered_at = models.DateTimeField(
        auto_now_add=True,
    )

    def get_absolute_url(self):
        return reverse('travelers:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name