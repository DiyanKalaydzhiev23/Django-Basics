from lib2to3.fixes.fix_input import context

from django.forms import modelformset_factory
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from books.models import Book
from reviews.forms import ReviewCreateForm, ReviewEditForm
from reviews.models import Review

DEFAULT_REVIEWS_COUNT = 5

def recent_reviews(request: HttpRequest) -> HttpResponse:
    reviews_count = int(request.GET.get('count', DEFAULT_REVIEWS_COUNT))  # http://localhost:8000/reviews/?count=3
    # request.GET -> {'count': 3}.get(count) -> 3 OR DEFAULT_REVIEWS_COUNT

    reviews = Review.objects.select_related('book')[:reviews_count]  # LIMIT 3;

    context = {
        'reviews': reviews,
        'page_title': 'Recent Reviews',
    }

    return render(request, 'reviews/list.html', context)


def review_details(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk,
    )

    context = {
        'review': review,
        'page_title': f'{review.author}\'s review on {review.book.title}'
    }

    return render(request, 'reviews/detail.html', context)


def review_create(request: HttpRequest) -> HttpResponse:
    form = ReviewCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('books:list')

    context = {
        'form': form,
        'page_title': f'Create Review'
    }

    return render(request, 'reviews/create.html', context)


def review_edit(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk,
    )
    form = ReviewEditForm(request.POST or None, instance=review)

    if form.is_valid():
        form.save()
        return redirect('books:list')

    context = {
        'form': form,
        'page_title': f'Edit Review'
    }

    return render(request, 'reviews/edit.html', context)


def review_delete(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk,
    )
    form = ReviewCreateForm(instance=review)

    if request.method == "POST":
        review.delete()
        return redirect('books:list')

    context = {
        'form': form,
        'page_title': f'Delete Review'
    }

    return render(request, 'reviews/delete.html', context)


def review_bulk_edit(request: HttpRequest, book_slug: str) -> HttpResponse:
    if not request.user.is_staff:
        raise Http404

    book = get_object_or_404(Book, slug=book_slug)
    ReviewFormSet = modelformset_factory(
        Review,
        form=ReviewEditForm,
        can_delete=True,
    )

    formset = ReviewFormSet(
        request.POST or None,
        queryset=Review.objects.filter(book=book),
    )

    if request.method == "POST" and formset.is_valid():
        instances = formset.save(commit=False)

        for instance in instances:
            instance.book = book
            instance.save()

        for instance in formset.deleted_objects:
            instance.delete()

        return redirect("reviews:list")

    context = {
        "formset": formset,
        "book": book,
    }

    return render(request, "reviews/formset_edit.html", context)


