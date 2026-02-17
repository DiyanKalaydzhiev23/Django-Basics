from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


class Album(models.Model):
    class Genre(models.TextChoices):
        POP_MUSIC = 'Pop Music', 'Pop Music'
        JAZZ_MUSIC = 'Jazz Music', 'Jazz Music'
        RB_MUSIC = 'R&B Music', 'R&B Music'
        ROCK_MUSIC = 'Rock Music', 'Rock Music'
        COUNTRY_MUSIC = 'Country Music', 'Country Music'
        DANCE_MUSIC = 'Dance Music', 'Dance Music'
        HIP_HOP_MUSIC = 'Hip Hop Music', 'Hip Hop Music'
        OTHER = 'Other', 'Other'

    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=Genre.choices,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[
            MinValueValidator(
                limit_value=0,
            )
        ]
    )

    owner = models.ForeignKey(
        "profiles.Profile",
        on_delete=models.CASCADE,
        related_name="albums",
    )
