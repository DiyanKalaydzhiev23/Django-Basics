from django import forms
from travelers.models import Traveler


class TravelForm(forms.ModelForm):
    class Meta:
        model = Traveler
        exclude = ["registered_at"]
        error_messages = {
            "age": {
                "min_value": "A traveler must be at least 18 years old",
            },
            "email": {
                "invalid": "Provide a valid university email address",
            },
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Joe Doe"}),
            "email": forms.EmailInput(attrs={"placeholder": "student@university.com/student@university.org"})
        }