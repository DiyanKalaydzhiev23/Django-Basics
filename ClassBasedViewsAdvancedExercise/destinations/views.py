from django.db.models import Avg
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from destinations.models import Destination



class DestinationCreateView(CreateView):
    model = Destination
    fields = "__all__"
    success_url = reverse_lazy('home')



class DestinationDetailView(DetailView):
    queryset = Destination.objects.prefetch_related('travelers', 'reviews__traveler').annotate(
        avg_rating=Avg('reviews__rating')
    )
