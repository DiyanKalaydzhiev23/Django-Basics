from lib2to3.fixes.fix_input import context

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from destinations.models import Destination
from reviews.models import Review


def dashboard(request: HttpRequest) -> HttpResponse:
    recent_destinations = Destination.objects.filter(is_active=True).order_by('-created_at')[:3]
    latest_reviews = Review.objects.filter(is_published=True).order_by('-created_at')[:3]

    context = {
        'recent_destinations': recent_destinations,
        'latest_reviews': latest_reviews,
    }

    return render(request, 'destinations/dashboard.html', context)


def destination_list(request: HttpRequest) -> HttpResponse:
    context = {
        'destinations': Destination.objects.all()
    }

    return render(request, 'destinations/list.html', context)


def destination_detail(request: HttpRequest, slug: str) -> HttpResponse:
    destination = get_object_or_404(Destination, slug=slug)  # Destination.objects.get(slug=slug)

    context = {
        "destination": destination,
    }

    return render(request, 'destinations/detail.html', context)


def redirect_softuni(request):
    return redirect('https://softuni.bg/')