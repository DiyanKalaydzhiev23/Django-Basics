from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from destinations.models import Destination
from travelers.models import Traveler


class Review(models.Model):
    class ReviewType(models.TextChoices):
        TEXT = "Text", "Text"
        VIDEO = "Video", "Video"
        AUDIO = "Audio", "Audio"

    body = models.TextField()
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(5.00)],
    )
    is_verified = models.BooleanField(
        default=False,
    )
    review_type = models.CharField(
        max_length=10,
        choices=ReviewType.choices,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    traveler = models.ForeignKey(
        Traveler,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    def clean(self) -> None:
        if self.destination_id and not self.destination.is_available:
            raise ValidationError("Cannot create review for unavailable destination")

    def __str__(self):
        return f"Review by {self.traveler} for {self.destination}"