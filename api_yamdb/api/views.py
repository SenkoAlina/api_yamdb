from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from rest_framework import filters, mixins, permissions, viewsets

from .filters import TitleFilterSet
from .permissions import AdminOrReadOnly
from .serializers import CategorySerializer, GenreSerializer, ReadOnlyTitleSerializer, TitleSerializer
from reviews.models import Category, Genre, Title


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pass


class CategoryViewSet(CreateListViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(CreateListViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        average_rating=Avg('reviews__score')).order_by('name')
    serializer_class = TitleSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilterSet

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return ReadOnlyTitleSerializer
        return TitleSerializer
