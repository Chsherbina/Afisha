from rest_framework import serializers
from .models import Director, Review, Movie


class DirectorSerializer(serializers.ModelSerializer):
    amount_movies = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = ['name', 'amount_movies']

    def get_amount_movies(self, obj):
        return obj.movies.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True)
    review_mean = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['title', 'director', 'reviews', 'description', 'duration', 'review_mean']

    def get_review_mean(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            summ = sum(i.stars for i in reviews)
            mean = round(summ/len(reviews), 1)
            return mean