from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, TemplateView

from albums.models import Album
from profiles.forms import ProfileForm
from profiles.models import Profile
from profiles.util import get_profile


class HomeView(View):
    def get(self, request) -> HttpResponse:
        profile = get_profile()

        context = {
            "form": ProfileForm(),
        }

        if not profile:
            return render(request, 'profiles/home-no-profile.html', context)

        all_albums = Album.objects.all()
        context["albums"] = all_albums

        return render(request, 'profiles/home-with-profile.html', context)

    def post(self, request) -> HttpResponse:
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("profiles:home")  # Todo: redirect to profile page

        return render(request, 'profiles/home-no-profile.html', {"form": form})


class ProfileDetailView(DetailView):
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None) -> Profile:
        return get_profile()

    def get_context_data(self, **kwargs) -> dict:
        kwargs.update({
            "albums_count": self.object.albums.count(),
        })
        return super().get_context_data(**kwargs)


class ProfileDeleteView(TemplateView):
    template_name = 'profiles/profile-delete.html'

    def post(self, request):
        get_profile().delete()
        return redirect('profiles:home')
