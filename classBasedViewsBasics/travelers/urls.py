from django.urls import path
from travelers import views

app_name = 'travelers'

urlpatterns = [
    path('create/', views.TravelerCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.TravelerUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TravelerDeleteView.as_view(), name='delete'),
]
