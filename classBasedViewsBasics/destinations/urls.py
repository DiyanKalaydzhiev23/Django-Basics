from django.urls import path

from destinations import views

app_name = 'destination'

urlpatterns = [
    path('create/', views.DestinationCreateView.as_view(), name='create')
]
