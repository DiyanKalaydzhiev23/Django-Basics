from django.http import HttpResponse
from django.shortcuts import render
from notes.models import Note


def dashboard(request) -> HttpResponse:
    query = request.GET.get('q')
    notes = Note.objects.prefetch_related('category').all()

    if query:
        notes = notes.filter(title__icontains=query)

    context = {
        'notes': notes,
        'query': query or "",
    }

    return render(request, 'index.html', context)
