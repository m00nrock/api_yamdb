from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import ReviewViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'titles/(?P<id>\d+)/reviews', ReviewViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
