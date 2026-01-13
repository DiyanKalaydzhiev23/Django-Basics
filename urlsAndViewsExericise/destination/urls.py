from django.urls import path, include
from destination.views import index, destinations_list, destination_detail, redirect_home

app_name = 'destination'

urlpatterns = [
    path('', index, name='index'),
    path('redirect-home/', redirect_home, name='redirect-home'),  # Better off placed in common app
    path('destinations/', include([
        path('', destinations_list, name='list'),
        path('detail/<slug:slug>/', destination_detail, name='detail'),
    ]))
]
