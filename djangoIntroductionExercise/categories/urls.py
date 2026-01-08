from django.urls import path

from categories import views

urlpatterns = [
    path('', views.list_categories, name='list-categories'),
]