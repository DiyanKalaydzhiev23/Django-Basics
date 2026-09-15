from lib2to3.fixes.fix_input import context

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404

from reviews.models import Review



def review_detail(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'reviews/detail.html', {'review': get_object_or_404(Review, pk=pk)})


def review_by_year(request: HttpRequest, year: int) -> HttpResponse:
    reviews = get_list_or_404(Review, created_at__year=year)

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews-by-year.html', context)