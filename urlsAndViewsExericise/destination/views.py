from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from destination.models import Destination
from review.models import Review


def index(request: HttpRequest) -> HttpResponse:
    featured_destinations = Destination.objects.filter(is_active=True).order_by('-created_at')[:3]
    latest_reviews = Review.objects.filter(is_published=True).order_by('-created_at')[:3]

    context = {
        'page_title': 'Welcome',
        'featured_destinations': featured_destinations,
        'latest_reviews': latest_reviews,
    }

    return render(request, 'home.html', context)


def destinations_list(request: HttpRequest) -> HttpResponse:
    destinations = Destination.objects.all()

    context = {
        'destinations': destinations,
        'page_title': 'All Destinations'
    }

    return render(request, 'destination/list.html', context)


def destination_detail(request: HttpRequest, slug: str) -> HttpResponse:
    destination = get_object_or_404(Destination, slug=slug)

    context = {
        'destination': destination,
        'page_title': f'{destination.name} Details',
    }

    return render(request, 'destination/detail.html', context)


def redirect_home(request: HttpRequest) -> HttpResponse:
    return redirect('destination:list')
