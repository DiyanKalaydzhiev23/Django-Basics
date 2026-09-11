from django.http import HttpResponse
from django.shortcuts import render

from notes.models import Note


def dashboard(request) -> HttpResponse:
    query = request.GET.get('q')
    notes = Note.objects.all()

    if query:
        notes = notes.filter(title__icontains=query)

    context = {
        "notes": notes,
        "query": query,
    }

    return render(request, 'notes/dashboard.html', context)
