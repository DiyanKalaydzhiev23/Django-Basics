from datetime import date
from random import choice
from typing import Any

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError

from books.models import Book, Tag
from books.validators import RangeValidator
from common.mixins import DisableFormFieldsMixin



# class BookFormBasic(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'placeholder': 'e.g. Done'})
#     )  # type=text

#     price = forms.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#         min_value=0,
#         validators=[
#             RangeValidator(0, 1000),
#         ],
#         widget=forms.NumberInput(attrs={'step': '2'}),
#         label='Price (USD)'
#     )
#
#     isbn = forms.CharField(
#         max_length=12,
#         min_length=10,
#     )
#
#     genre = forms.ChoiceField(
#         choices=Book.GenreChoices.choices,
#     )
#
#     publishing_date = forms.DateField(
#         initial=date.today,
#     )
#
#     description = forms.CharField(
#         widget=forms.Textarea
#     )
#
#     image_url = forms.URLField()
#
#     publisher = forms.CharField(
#         max_length=100,
#     )

class BookFormBasic(forms.ModelForm):
    tags = forms.CheckboxSelectMultiple()

    field_order = [
        'title',
        'pages',
        'price',
    ]
    
    class Meta:
        exclude = ['slug']
        model = Book

        error_messages = {
            'title': {
                'max_length': 'The title is too long, no one is going to read that',
                'required': 'Hey you missed the title, no one is going to buy it',
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Keep crispy helper attrs visible on rendered form and load tag options
        self.fields['tags'].queryset = Tag.objects.all()
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))

    def clean_isbn(self) -> None:
        if self.cleaned_data["isbn"].startswith("978"):
            raise ValidationError("ISBN cannot start with 978")

    def clean(self) -> dict:
        cleaned = super().clean()

        genre = cleaned.get('genre')
        pages = cleaned.get('pages')

        if pages < 10 and genre == Book.GenreChoices.FICTION:
            raise ValidationError(f"Book of type {Book.GenreChoices.FICTION} cannot be less than 10 pages")

        return cleaned

    def save(self, commit=True):
        if self.publisher:
            self.publisher = self.publisher.capitalize()

        if commit:
            self.instance.save()

        return self.instance


class BookCreateForm(BookFormBasic):
    ...


class BookEditForm(BookFormBasic):
    ...


class BookDeleteForm(DisableFormFieldsMixin, BookFormBasic):
    ...
    # class Meta(BookFormBasic.Meta):
    #     widgets = {
    #         'title': forms.TextInput(
    #             attrs={'disabled': True}
    #         )
    #     }



class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,
    )
