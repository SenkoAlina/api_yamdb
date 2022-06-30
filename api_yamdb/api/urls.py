from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, ReviewViewSet, CategoryViewSet, GenreViewSet, TitleViewSet

app_name = 'api'

router = SimpleRouter()

router.register('categories', CategoryViewSet, basename='categorys')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register(r'titles/(?P<title_id>[\d]+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>[\d]+)'
                r'/reviews/(?P<review_id>[\d]+)/comments', CommentViewSet,
                basename='comments')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
