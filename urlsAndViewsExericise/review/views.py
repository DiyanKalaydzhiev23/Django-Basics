from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from review.models import Review


DEFAULT_REVIEW_COUNT: int = 5


def recent_reviews(request: HttpRequest) -> HttpResponse:
    review_count = request.GET.get(
        key='review_count',
        default=DEFAULT_REVIEW_COUNT
    )
    reviews = Review.objects.filter(
        is_published=True
    ).order_by('-created_at')[:int(review_count)]

    context = {
        'reviews': reviews,
        'page_title': 'Recent reviews',
    }

    return render(request, 'review/list.html', context)


def review_detail(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)

    context = {
        'review': review,
        'page_title': f'{review.author}\'s review on {review.destination.name}'
    }

    return render(request, 'review/detail.html', context)


def reviews_by_year(request: HttpRequest, year: int) -> HttpResponse:
    reviews = Review.objects.filter(created_at__year=year)

    context = {
        'reviews': reviews,
        'page_title': f'Reviews for {year}',
    }

    return render(request, 'review/list.html', context)
