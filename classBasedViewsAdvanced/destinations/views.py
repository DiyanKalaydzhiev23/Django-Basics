from django.db.models import Avg
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from destinations.forms import DestinationForm
from destinations.models import Destination


class DestinationCreateView(CreateView):
    model = Destination
    form_class = DestinationForm
    success_url = reverse_lazy('common:home')


class DestinationDetailView(DetailView):
    queryset = Destination.objects.prefetch_related('travelers', 'reviews').annotate(
        avg_rating=Avg('reviews__rating')
    )
