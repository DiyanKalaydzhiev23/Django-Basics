from django.urls import reverse_lazy
from django.views.generic import CreateView
from destinations.models import Destination


class DestinationCreateView(CreateView):
    model = Destination
    fields = "__all__"
    success_url = reverse_lazy('home')
