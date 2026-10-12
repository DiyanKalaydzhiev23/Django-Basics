from django.urls import path

from travelers.views import TravelerCreateView, TravelerUpdateView, TravelerDeleteView

urlpatterns = [
    path('create/', TravelerCreateView.as_view(), name='traveler-create'),
    path('edit/<int:pk>/', TravelerUpdateView.as_view(), name='traveler-update'),
    path('delete/<int:pk>/', TravelerDeleteView.as_view(), name='traveler-delete'),
]