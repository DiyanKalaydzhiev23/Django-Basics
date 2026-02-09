from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.timezone import now
from django.views import View
from django.views.generic import TemplateView, RedirectView

from travelers.models import Traveler


class WelcomeView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return HttpResponse(status=403)

        return super().dispatch(request, *args, **kwargs)

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Welcome to our travel app!")

    def post(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Post was called")


class HomeView(TemplateView):
    def get_context_data(self, **kwargs):
        kwargs.update({
            "current_time": str(now()),
            "travelers_count": Traveler.objects.count()
        })
        return super().get_context_data(**kwargs)

    def get_template_names(self) -> list[str]:
        if self.request.user.is_staff:
            return ['admin_home.html']

        return ['home.html']

class HomeTeenWelcomeView(TemplateView):
    template_name = 'teen_welcome.html'


class AgeCheckRedirectView(RedirectView):
    permanent = False  # By default false

    def get_redirect_url(self, *args, **kwargs) -> str:
        pk = self.request.GET.get('pk')
        traveler = get_object_or_404(Traveler, pk=pk)

        if traveler.age > 21:
            return reverse('common:home')

        return reverse('common:home-teen')
