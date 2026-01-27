from django.urls import path, include
from books.views import landing_page, books_list, book_detail, book_create, book_edit, book_delete

app_name = 'books'

books_patterns = [
    path('', books_list, name='list'),
    path('create/', book_create, name='create'),
    path('<int:pk>/', include([
        path('edit/', book_edit, name='edit'),
        path('delete/', book_delete, name='delete'),
    ])),
    path('<slug:slug>/', book_detail, name='details'),
]

urlpatterns = [
    path('', landing_page, name='home'),
    path('books/', include(books_patterns)),
]