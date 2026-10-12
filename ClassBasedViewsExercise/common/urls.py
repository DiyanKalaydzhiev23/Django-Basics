from django.urls import path
from common.views import WelcomeView, HomeView, BulgarianHomeView, CountryRedirectView

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('home/', HomeView.as_view(), name='home'),
    path('home-bulgaria/', BulgarianHomeView.as_view(), name='bulgaria-home'),
    path('redirect/', CountryRedirectView.as_view(), name='redirect'),
]