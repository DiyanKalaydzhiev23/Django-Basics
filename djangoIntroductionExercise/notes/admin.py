from django.contrib import admin
from notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    ...
