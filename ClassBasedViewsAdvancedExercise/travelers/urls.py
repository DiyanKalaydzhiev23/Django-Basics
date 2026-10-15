from django.urls import path

from travelers.models import Traveler
from travelers.views import TravelerCreateView, TravelerUpdateView, TravelerDeleteView, TravelerDetailView, \
    TravelerListView

urlpatterns = [
    path('create/', TravelerCreateView.as_view(), name='traveler-create'),
    path('edit/<int:pk>/', TravelerUpdateView.as_view(), name='traveler-update'),
    path('delete/<int:pk>/', TravelerDeleteView.as_view(), name='traveler-delete'),
    path('<int:pk>/', TravelerDetailView.as_view(), name='traveler-detail'),
    path('', TravelerListView.as_view(), name='traveler-list'),
]