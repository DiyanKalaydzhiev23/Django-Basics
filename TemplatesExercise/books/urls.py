from django.urls import path, include
from books.views import landing_page, books_list, book_detail

app_name = 'books'

books_patterns = [
    path('', books_list, name='list'),
    path('<slug:slug>/', book_detail, name='details'),
]

urlpatterns = [
    path('', landing_page, name='home'),
    path('books/', include(books_patterns)),
]