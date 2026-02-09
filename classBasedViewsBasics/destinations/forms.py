from django import forms
from destinations.models import Destination


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        exclude = ['updated_at', 'slug']
