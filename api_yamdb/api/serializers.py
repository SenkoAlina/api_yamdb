from django.contrib.auth import get_user_model
from rest_framework import serializers

from reviews.models import Comment, Review, Category, Genre, Title

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = 'id', 'text', 'author', 'pub_date'
        model = Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = 'name', 'slug'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = 'name', 'slug'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TitleSerializer(serializers.ModelSerializer):

    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        many=True, slug_field='slug')

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug')

    class Meta:
        model = Title
        fields = 'id', 'name', 'year', 'rating', 'description', 'genre', 'category',


class ReadOnlyTitleSerializer(serializers.ModelSerializer):

    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField()

    class Meta:
        model = Title
        fields = 'id', 'name', 'year', 'rating', 'description', 'genre', 'category',

