from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'price']
