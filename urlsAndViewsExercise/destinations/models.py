from django.db import models
from django.utils.text import slugify

from urlsAndViewsExercise.models import TimestampMixin


class Destination(TimestampMixin):
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
        default=True,
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug and self.name and self.country:
            self.slug = slugify(f"{self.name}-{self.country}")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.slug
