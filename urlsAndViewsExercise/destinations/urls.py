from django.urls import path, include
from .views import dashboard, destination_list, destination_detail, redirect_softuni

app_name = 'destinations'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('destinations/', include([
        path('', destination_list, name='list'),  # destinations:list
        path('<slug:slug>/', destination_detail, name='detail'),
    ])),
    path('redirect/', redirect_softuni, name='redirect')  # better off in a common app
]