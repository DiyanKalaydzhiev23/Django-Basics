from django.urls import reverse_lazy
from django.views.generic import CreateView
from albums.forms import AlbumCreateForm
from albums.models import Album
from profiles.util import get_profile


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    success_url = reverse_lazy("profiles:home")
    template_name = 'albums/album-add.html'

    def get_initial(self) -> dict:
        initial = super().get_initial()
        initial["owner"] = get_profile()
        return initial

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)
