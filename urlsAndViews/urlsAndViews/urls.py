from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('departments/', include("department.urls")),
    path('admin/', admin.site.urls),
]
