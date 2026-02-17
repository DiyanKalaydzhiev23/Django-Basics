from django.urls import path

from albums import views

app_name = 'albums'

urlpatterns = [
    path('create/', views.AlbumCreateView.as_view(), name='create')
]