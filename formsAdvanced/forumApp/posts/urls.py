from django.urls import path, include
from posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('post/', include([
        path('add/', views.add_post, name='add-post'),
        path('edit/<int:pk>/', views.edit_post, name='edit-post'),
        path('delete/<int:pk>/', views.delete_post, name='delete-post'),
        path('details/<int:pk>/', views.post_details, name='post-details'),
    ])),
]