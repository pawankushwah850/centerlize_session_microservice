from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'^user', UserViewSet, basename="registration")
router.register(r'^user/userlogin', UserViewSet, basename="userlogin")
router.register(r'^user/userlogout', UserViewSet, basename="userlogout")

urlpatterns = [
    path('', include(router.urls))
]
