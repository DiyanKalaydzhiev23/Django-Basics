from django.core.exceptions import BadRequest
from django.db.models import Avg, Count, Q, QuerySet
from django.views.generic import ListView
from reviews.models import Review


class ReviewListView(ListView):
    queryset = Review.objects.select_related('traveler', 'destination')
    ordering = '-created_at'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = Review.objects.aggregate(
            avg_rating=Avg('rating'),
            verified_count=Count('pk', filter=Q(is_verified=True)),
            destinations_count=Count('destination', distinct=True),
        )
        return context

    def get_queryset(self) -> QuerySet[Review]:
         review_type = self.request.GET.get('type')
         verified = self.request.GET.get('verified') == "true"

         qs = super().get_queryset()

         if review_type:
             if review_type not in Review.ReviewType.values:
                raise BadRequest(f"Invalid review type: {review_type}")

             qs = qs.filter(review_type=review_type)

         if verified:
            qs = qs.filter(is_verified=verified)

         return qs


class VerifiedReviewListView(ListView):
     queryset = Review.objects.filter(is_verified=True)
