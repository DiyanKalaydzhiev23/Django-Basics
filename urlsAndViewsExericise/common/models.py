from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        abstract = True
