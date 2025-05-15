from django.contrib import admin
from todo_app.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ...
