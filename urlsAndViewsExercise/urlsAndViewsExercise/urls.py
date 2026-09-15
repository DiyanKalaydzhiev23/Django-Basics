from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('destinations.urls')),
    path('reviews/', include('reviews.urls')),
]
