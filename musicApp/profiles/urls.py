from django.urls import path
from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('details/', views.ProfileDetailView.as_view(), name='detail'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete')
]