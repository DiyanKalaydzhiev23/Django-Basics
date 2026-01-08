from django.http import HttpResponse
from django.shortcuts import render

from categories.models import Category


def list_categories(request) -> HttpResponse:
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'list_categories.html', context)
