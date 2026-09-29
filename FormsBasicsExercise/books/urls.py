from django.urls import path, include
from books import views

app_name = 'books'  # books:landing-page, books:list, books:detail

urlpatterns = [
    path('', views.landing_page, name='landing-page'),  # /
    path('books/', include([
        path('', views.books_list, name='list'),  # books/
        path('create/', views.book_create, name='create'),
        path('<slug:slug>/', include([
            path('', views.book_detail, name='detail'),
            path('edit/', views.book_edit, name='edit'),
            path('delete/', views.book_delete, name='delete'),
        ])),  # books/slug/
    ]))
]