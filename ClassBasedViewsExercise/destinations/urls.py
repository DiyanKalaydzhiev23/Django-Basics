from django.urls import path

from destinations.views import DestinationCreateView

urlpatterns = [
    path('create/', DestinationCreateView.as_view(), name='destination-create'),
]