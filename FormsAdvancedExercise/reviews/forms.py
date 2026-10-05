from decimal import Decimal
from distutils.command.clean import clean

from django import forms
from django.core.exceptions import ValidationError

from FormsAdvancedExercise.mixins import DisabledFormMixin
from reviews.models import Review


class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

    def clean_rating(self) -> Decimal:
        rating = self.cleaned_data["rating"]

        if not 0 < rating < 5:
            raise ValidationError("Rating must be between 0 and 5")

        return rating

    def clean(self) -> dict:
        cleaned_data = super().clean()
        if cleaned_data.get('is_spoiler') and not cleaned_data.get("body"):
            self.add_error("body", "Marking as spoiler must include a body")

        return cleaned_data


class ReviewCreateForm(ReviewBaseForm):
    ...


class ReviewEditForm(ReviewBaseForm):
    ...


class ReviewDeleteForm(DisabledFormMixin, ReviewBaseForm):
    ...
