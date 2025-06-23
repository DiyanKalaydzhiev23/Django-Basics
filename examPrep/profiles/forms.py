from django import forms
from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age',
                }
            ),
        }


class ProfileCreateForm(ProfileBaseForm):
    ...
