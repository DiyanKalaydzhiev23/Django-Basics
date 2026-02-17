from django.urls import path

from albums import views

app_name = 'albums'

urlpatterns = [
    path('create/', views.AlbumCreateView.as_view(), name='create'),
    path('details/<int:pk>/', views.AlbumDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.AlbumEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.AlbumDeleteView.as_view(), name='delete'),
]