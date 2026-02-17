from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from albums.forms import AlbumCreateForm, AlbumEditForm
from albums.mixins import AttachOwnerMixin
from albums.models import Album
from profiles.util import get_profile


class AlbumCreateView(AttachOwnerMixin, CreateView):
    model = Album
    form_class = AlbumCreateForm
    success_url = reverse_lazy("profiles:home")
    template_name = 'albums/album-add.html'


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/album-details.html'


class AlbumEditView(AttachOwnerMixin, UpdateView):
    model = Album
    form_class = AlbumEditForm
    template_name = 'albums/album-edit.html'

    def get_success_url(self) -> str:
        return reverse('albums:detail', kwargs={'pk': self.object.pk})
