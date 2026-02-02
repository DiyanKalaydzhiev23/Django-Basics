from django.urls import path, include

from reviews.views import recent_reviews, review_details, review_create, review_edit, review_delete, review_bulk_update

app_name = 'reviews'

reviews_patterns = [
    path('', recent_reviews, name='list'),
    path('create/', review_create, name='create'),
    path('<slug:book_slug>/', review_bulk_update, name='bulk-update'),
    path('<int:pk>/', include([
        path('', review_details, name='details'),
        path('edit/', review_edit, name='edit'),
        path('delete/', review_delete, name='delete'),
    ])),
]

urlpatterns = [
    path('', include(reviews_patterns)),
]
