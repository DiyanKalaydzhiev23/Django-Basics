from django import forms
from FormsAdvancedExercise.mixins import DisabledFormMixin
from books.models import Book, Tags


# class BookFormBasic(forms.ModelForm):
#     title = forms.CharField(
#         max_length=100,
#         # widget=forms.Textarea(attrs={'placeholder': 'e.g. Done'})
#     )
#     price = forms.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#     )
#     isbn = forms.CharField(
#         max_length=12,
#     )


class BookBaseForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    # field_order = [
    #     'isbn',
    #     'title',
    #     'price',
    # ]

    class Meta:
        model = Book
        exclude = ['slug']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Insert title here'})
        }
        error_messages = {
            'isbn': {
                'unique': 'ISBN should be unique, we already have a book with this isbn',
            }
        }


class BookCreateForm(BookBaseForm):
    ...


class BookEditForm(BookBaseForm):
    ...


class BookDeleteForm(DisabledFormMixin, BookBaseForm):
    ...


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
    )
