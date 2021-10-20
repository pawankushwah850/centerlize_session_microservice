from django.urls import path
from .views import see_user_is_exits

urlpatterns = [
    path('getProfile', see_user_is_exits, name="see_user_is_exits")
]
