from django.db import models
from common.models import TimeStampModel


class Review(TimeStampModel):
    author = models.CharField(
        max_length=100,
    )

    body = models.TextField()

    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    is_spoiler = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ['-created_at']
