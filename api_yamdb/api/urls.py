from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import SignUp, GetToken, UsersViewSet

router_v1 = SimpleRouter()
router_v1.register(r'users', UsersViewSet)

urlpatterns = [
    path('v1/auth/token/', GetToken.as_view()),
    path('v1/auth/signup/', SignUp.as_view()),
    path('v1/', include(router_v1.urls)),
]
