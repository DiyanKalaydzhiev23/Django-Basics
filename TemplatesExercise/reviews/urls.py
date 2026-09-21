from django.urls import path
from reviews import views

app_name = 'reviews'  # reviews:list, reviews:details

urlpatterns = [
    path('', views.recent_reviews, name='list'),
    path('<int:pk>/', views.review_details, name='details'),
]