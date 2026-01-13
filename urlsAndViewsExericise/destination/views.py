from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from destination.models import Destination


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Welcome to our travel application!')


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
