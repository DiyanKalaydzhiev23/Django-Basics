

from django.urls import path, include
from reviews import views

app_name = 'reviews'  # reviews:list, reviews:details

urlpatterns = [
    path('', views.recent_reviews, name='list'),
    path('create/', views.review_create, name='create'),
    path('<int:pk>/', include([
        path('', views.review_details, name='details'),
        path('edit/', views.review_edit, name='edit'),
        path('delete/', views.review_delete, name='delete'),
    ])),
]