from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
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


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy("profiles:home")

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)
