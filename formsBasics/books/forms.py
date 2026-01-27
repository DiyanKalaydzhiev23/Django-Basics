from datetime import date
from random import choice
from typing import Any

from django import forms

from books.models import Book, Tag
from common.mixins import DisableFormFieldsMixin


#
# class BookFormBasic(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'placeholder': 'e.g. Done'})
#     )  # type=text
#
#     price = forms.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#         min_value=0,
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
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()


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
