from django.urls import path
from .views import (movies, movie_detail,
                    directors, director_detail,
                    reviews, review_detail)

urlpatterns = [
    path('', movies),
    path('<int:pk>/', movie_detail),
    path('reviews/', reviews),
    path('reviews/<int:pk>/', review_detail),
    path('directors/', directors),
    path('directors/<int:pk>/', director_detail),
]