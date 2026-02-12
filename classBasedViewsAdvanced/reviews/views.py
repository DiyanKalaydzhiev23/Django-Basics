from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from common.mixins import AgeRestrictionMixin
from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewCreateView(AgeRestrictionMixin, CreateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('common:home')


class ReviewList(ListView):
    ordering = ['-created_at']
    paginate_by = 1

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page_message'] = f"You are on page {context['page_obj'].number}"
    #     return context

    def get_paginate_by(self, queryset):
        per_page_param = self.request.GET.get('per_page')  # ?per_page=10

        if per_page_param:
            try:
                return int(per_page_param)
            except (TypeError, ValueError):
                pass

        return super().get_paginate_by(queryset)

    def get_queryset(self) -> QuerySet[Review]:
        qs = Review.objects.filter(is_verified=True)
        review_type = self.request.GET.get('type')

        if review_type:
            if review_type not in Review.ReviewType.labels:
                raise HttpResponseBadRequest

            qs = qs.filter(review_type=review_type)

        return qs
