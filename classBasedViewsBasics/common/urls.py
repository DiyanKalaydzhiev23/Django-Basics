from django.urls import path
from common import views

app_name = "common"

urlpatterns = [
    path('', views.WelcomeView.as_view(), name="welcome"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('teen/', views.HomeTeenWelcomeView.as_view(), name="home-teen"),
    path('age-check/', views.AgeCheckRedirectView.as_view(), name='age-check'),
    # path('home/', views.TemplateView.as_view(template_name='home.html')),
]
