from django.db.models import QuerySet, Avg
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from books.models import Book


def _with_rating(queryset) -> QuerySet:
    return queryset.annotate(
        avg_rating=Avg('reviews__rating')
    )


def landing_page(request: HttpRequest) -> HttpResponse:
    total_books_count = Book.objects.count()  # 100
    latest_book = Book.objects.order_by('-publishing_date').first()  # PB Basics Softuni

    context = {
        'total_books_count': total_books_count,
        'latest_book': latest_book,
        'page_title': 'Home',
    }

    return render(request, 'books/landing_page.html', context)


def books_list(request: HttpRequest) -> HttpResponse:
    books = _with_rating(Book.objects.all())

    context = {
        'books': books,
        'page_title': 'Dashboard',
    }

    return render(request, 'books/list.html', context)


def book_detail(request: HttpRequest, slug: str):
    book = get_object_or_404(_with_rating(Book.objects), slug=slug)

    context = {
        'book': book,
        'page_title': f'{book.title} details'  # PB Basics By Nakov details
    }

    return render(request, 'books/detail.html', context)
