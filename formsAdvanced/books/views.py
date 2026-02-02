from django.db.models import Avg, Q
from django.forms import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookFormBasic, BookCreateForm, BookEditForm, BookDeleteForm, BookSearchForm
from books.models import Book


def landing_page(request: HttpRequest) -> HttpResponse:
    total_books = Book.objects.count()
    latest_book = Book.objects.order_by('-publishing_date').first()

    context = {
        'total_books': total_books,
        'latest_book': latest_book,
        'page_title': 'Home',
    }

    return render(request, 'books/landing_page.html', context)


def books_list(request: HttpRequest) -> HttpResponse:
    search_form = BookSearchForm(request.GET or None)

    list_books = Book.objects.annotate(
        avg_rating=Avg('reviews__rating'),
    ).order_by('title')

    if 'query' in request.GET:
        if search_form.is_valid():
            search_value = search_form.cleaned_data['query']
            list_books = list_books.filter(
                Q(title__icontains=search_value)
                    |
                Q(description__icontains=search_value)
            )

    context = {
        'books': list_books,
        'page_title': 'Dashboard',
        'search_form': search_form,
    }

    return render(request, 'books/list.html', context)


def book_detail(request: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(
        Book.objects.annotate(
            avg_rating=Avg('reviews__rating'),
        ),
        slug=slug,
    )

    context = {
        'book': book,
        'page_title': f'{book.title} details'
    }

    return render(request, 'books/detail.html', context)


def book_create(request: HttpRequest) -> HttpResponse:
    if request.user.is_staff:
        BookForm = modelform_factory(Book, fields='__all__')
    else:
        BookForm = modelform_factory(Book, exclude=['slug'])

    form = BookForm(request.POST or None, request.FILES)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('books:home')

    context = {
        "form": form,
    }

    return render(request, 'books/create.html', context)


def book_edit(request: HttpRequest, pk: int) -> HttpResponse:
    book = Book.objects.get(pk=pk)
    form = BookEditForm(request.POST or None, instance=book)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('books:home')

    context = {
        "form": form,
    }

    return render(request, 'books/edit.html', context)


def book_delete(request: HttpRequest, pk: int) -> HttpResponse:
    book = Book.objects.get(pk=pk)
    form = BookDeleteForm(request.POST or None, instance=book)

    if request.method == "POST" and form.is_valid():
        book.delete()
        return redirect('books:home')

    context = {
        "form": form,
    }

    return render(request, 'books/delete.html', context)
