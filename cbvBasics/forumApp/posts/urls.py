from datetime import datetime

from django.urls import path, include
from posts import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('post/', include([
        path('add/', views.CreatePost.as_view(), name='add-post'),
        path('edit/<int:pk>/', views.EditPost.as_view(), name='edit-post'),
        path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete-post'),
        path('details/<int:pk>/', views.post_details, name='post-details'),
    ])),
    path('redirect/', views.MyRedirectView.as_view()),
]