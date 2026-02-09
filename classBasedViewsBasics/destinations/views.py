from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from destinations.forms import DestinationForm
from destinations.models import Destination


class DestinationCreateView(CreateView):
    model = Destination
    form_class = DestinationForm
    success_url = reverse_lazy('common:home')
