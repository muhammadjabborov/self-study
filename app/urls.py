from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import AuthorModelViewSet, BlogModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('blogs', BlogModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
