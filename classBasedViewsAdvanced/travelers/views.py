from lib2to3.fixes.fix_input import context

from django.contrib import messages
from django.db.models import QuerySet
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from common.mixins import RecentObjectsMixin
from travelers.forms import TravelForm
from travelers.models import Traveler


class TravelerCreateView(CreateView):
    model = Traveler
    form_class = TravelForm
    success_url = reverse_lazy('common:home')
    # template_name = 'travelers/traveler_form.html'  # by default

    def form_valid(self, form):
        messages.success(self.request, "Traveler successfully created")
        return super().form_valid(form)


class TravelerUpdateView(UpdateView):
    model = Traveler
    form_class = TravelForm
    success_url = reverse_lazy('common:home')


class TravelerDeleteView(DeleteView):
    model = Traveler
    success_url = reverse_lazy('common:home')


class TravelerDetailView(DetailView):
    model = Traveler

    http_method_names = ['get']

    # def dispatch(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #         raise HttpResponseForbidden
    #
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data()
        context['reviews_count'] = self.object.reviews.count()
        return context


class TravelerListView(RecentObjectsMixin, ListView):
    paginate_by = 3
    recent_results_limit = 2
    ordering = ['-name']

    def get_queryset(self) -> QuerySet[Traveler]:
        qs = Traveler.objects.filter(age__gte=21)
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(name__icontains=query)

        return qs