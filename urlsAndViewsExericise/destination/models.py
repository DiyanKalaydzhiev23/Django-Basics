from django.db import models
from django.template.defaultfilters import slugify

from common.models import TimeStampModel


class Destination(TimeStampModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    slug = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
    )
    description = models.TextField()
    country = models.CharField(
        max_length=100,
    )
    is_active = models.BooleanField(
        default=True
    )

    def save(self, *args, **kwargs):
        if not self.slug and self.name and self.country:
            self.slug = slugify(f"{self.name}-{self.country}")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - {self.country}"
