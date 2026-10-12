from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now
from django.views import View
from django.views.generic import TemplateView, RedirectView

from common.choices import CountryChoice
from travelers.models import Traveler


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Welcome to out travel app!')


class HomeView(TemplateView):
    # template_name = 'home.html' # static way
    # extra_context = {
    #     'current_time': now(),
    # }  # static way

    def get_template_names(self):
        traveler = Traveler.objects.first()

        if traveler and traveler.age > 18:
            return ['home.html']

        return ['teen_welcome.html']

    def get_context_data(self, **kwargs):
        kwargs.update({
            'current_time': now(),
        })
        return super().get_context_data(**kwargs)


class BulgarianHomeView(TemplateView):
    template_name = 'bulgarian_template.html'


class CountryRedirectView(RedirectView):
    # url = 'http://127.0.0.1:8000/home-bulgaria/'
    # pattern_name = 'bulgaria-home'

    def get_redirect_url(self, *args, **kwargs):
        traveler = Traveler.objects.first()

        if traveler and traveler.country == CountryChoice.BULGARIA.value:
            return reverse('bulgaria-home')

        return reverse('home')