from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from reviews.models import Review


def recent_reviews(request: HttpRequest) -> HttpResponse:
    DEFAULT_REVIEWS_COUNT = 5
    reviews_count = int(request.GET.get('count', DEFAULT_REVIEWS_COUNT))

    reviews = Review.objects.select_related('book')[:reviews_count]

    context = {
        'reviews': reviews,
        'page_title': 'Recent reviews',
    }

    return render(request, 'reviews/list.html', context)


def review_details(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk,
    )

    context = {
        'review': review,
        'page_title': f'{review.author}\'s review on {review.book.title}',
    }

    return render(request, 'reviews/detail.html', context)
