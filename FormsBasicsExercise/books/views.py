from django.db.models import QuerySet, Avg
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookCreateForm, BookEditForm, BookDeleteForm, SearchForm
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
    search_form = SearchForm(request.GET or None)

    if request.GET and search_form.is_valid():
        books = books.filter(title__icontains=search_form.cleaned_data['query'])

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


def book_create(request: HttpRequest) -> HttpResponse:
    form = BookCreateForm(request.POST or None)

    if form.is_valid():
        form.save()  # Only on model forms
        return redirect('books:landing-page')

    context = {
        'form': form,
    }

    return render(request, 'books/create.html', context)


def book_edit(request: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    form = BookEditForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()  # Only on model forms
        return redirect('books:landing-page')

    context = {
        'form': form,
    }

    return render(request, 'books/edit.html', context)


def book_delete(request: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    form = BookDeleteForm(instance=book)

    if request.method == "POST":
        book.delete()
        return redirect('books:landing-page')

    context = {
        'form': form,
    }

    return render(request, 'books/delete.html', context)