from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse(f"Welcome to the forum app!")


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to work with templates?",
                "author": "Diyan Kalaydzhiev",
                "content": "**Hey** how <i>can</i> i work with templates in Django? I am really bad at this. My first time using them.",
                "created_at": datetime.now(),
            },
            {
                "title": "was dido lecture good?",
                "author": "Anonymous",
                "content": "Should i watch it?",
                "created_at": datetime.now(),
            },
            {
                "title": "What is the next lecture?",
                "author": "",
                "content": "Hey guys i have no idea, pls answer!!!",
                "created_at": datetime.now(),
            },
        ],
    }

    return render(request, 'base.html', context)