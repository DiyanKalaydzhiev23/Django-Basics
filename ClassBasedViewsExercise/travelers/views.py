from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from travelers.forms import TravelForm
from travelers.models import Traveler


class TravelerCreateView(CreateView):
    model = Traveler
    form_class = TravelForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Traveler successfully created")
        return super().form_valid(form)


class TravelerUpdateView(UpdateView):
    model = Traveler
    form_class = TravelForm
    success_url = reverse_lazy('home')


class TravelerDeleteView(DeleteView):
    model = Traveler
    success_url = reverse_lazy('home')

