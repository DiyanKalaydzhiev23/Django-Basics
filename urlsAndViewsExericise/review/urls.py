from django.urls import path, re_path
from review.views import recent_reviews, review_detail, reviews_by_year

app_name = 'review'

urlpatterns = [
    path('', recent_reviews, name='list'),
    re_path(r'^(?P<year>20\d{2})/$', reviews_by_year, name='list-year'),
    path('details/<int:pk>/', review_detail, name='detail'),
]