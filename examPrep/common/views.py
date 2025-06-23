from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from albums.models import Album
from common.utils import get_profile
from profiles.forms import ProfileCreateForm


class HomePage(ListView, FormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self) -> list[str]:
        if not get_profile():
            return ['home-no-profile.html']

        return ['home-with-profile.html']

    def form_valid(self, form: ProfileCreateForm) -> HttpResponseRedirect:
        if form.is_valid():
            form.save()
            return super().form_valid(form)
