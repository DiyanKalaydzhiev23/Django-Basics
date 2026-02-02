from typing import Any

from django import forms

from common.mixins import DisableFormFieldsMixin
from reviews.models import Review


class ReviewFormBasic(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateForm(ReviewFormBasic):
    ...


class ReviewEditForm(ReviewFormBasic):
    ...


class ReviewDeleteForm(DisableFormFieldsMixin, ReviewFormBasic):
    ...