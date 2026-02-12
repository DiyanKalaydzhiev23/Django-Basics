from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('create/', views.ReviewCreateView.as_view(), name='create'),
    path('', views.ReviewList.as_view(), name='list'),
]
