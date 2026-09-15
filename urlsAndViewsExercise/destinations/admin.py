from django.contrib import admin
from unfold.admin import ModelAdmin
from destinations.models import Destination


@admin.register(Destination)
class DestinationAdmin(ModelAdmin):
    ...
