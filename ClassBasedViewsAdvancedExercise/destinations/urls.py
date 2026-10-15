from django.urls import path, include

from destinations.views import DestinationCreateView, DestinationDetailView

urlpatterns = [
    path('create/', DestinationCreateView.as_view(), name='destination-create'),
    path('<int:pk>/', include([
        path('', DestinationDetailView.as_view(), name='destination-detail')
    ])),
]