from django.urls import path, re_path
from .views import review_by_year, review_detail

urlpatterns = [
    path('<int:pk>/', review_detail, name='review-detail'),
    re_path(r'year/^(?P<year>20\d{2})/$', review_by_year, name='review-by-year')
]