from django import forms
from travelers.models import Traveler


class TravelForm(forms.ModelForm):
    class Meta:
        model = Traveler
        exclude = ['registered_at']
        error_messages = {
            'age': {
                'min_value': 'A traveler must be at least 16 years old'
            },
            'email': {
                'invalid': 'Email is not from a university!',
            }
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'student@university.com/student@university.org'
            })
        }
