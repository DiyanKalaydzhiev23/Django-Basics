from django.shortcuts import render
from django.template.defaultfilters import title

from todo_app.models import Task


def index(request):
    search_title = request.GET.get('title_filter')
    tasks = Task.objects.filter(name__icontains=search_title)

    context = {
        "tasks": tasks,
        "search_title": search_title,
    }

    return render(request, "index.html", context)
