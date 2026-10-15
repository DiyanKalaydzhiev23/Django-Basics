from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
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



class TravelerDetailView(DetailView):
    model = Traveler

    def get_context_data(self, **kwargs) -> dict:
        reviews = self.object.reviews.select_related('destination')

        kwargs.update({
            "reviews": reviews,
            "destinations": self.object.destinations.all(),
            "reviews_count": len(reviews),
        })

        return super().get_context_data(**kwargs)


class TravelerListView(LoginRequiredMixin, ListView):
    paginate_by = 3
    login_url = '/admin/'
    ordering = ['-name']
