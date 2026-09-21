from django.urls import path, include
from books import views

app_name = 'books'  # books:landing-page, books:list, books:detail

urlpatterns = [
    path('', views.landing_page, name='landing-page'),  # /
    path('books/', include([
        path('', views.books_list, name='list'),  # books/
        path('<slug:slug>/', views.book_detail, name='detail'),  # books/slug/
    ]))
]