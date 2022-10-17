from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from root import settings
from app.views import PostModelViewSet

router = DefaultRouter()
router.register('post', PostModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
