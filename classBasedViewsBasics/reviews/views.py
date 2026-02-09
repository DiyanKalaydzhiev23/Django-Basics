from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('common:home')