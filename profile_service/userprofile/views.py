from django.http.response import JsonResponse,HttpResponse
from django.core.cache import cache
from django.contrib.auth.middleware import AuthenticationMiddleware

def see_user_is_exits(request):
    print(request.user)
    return HttpResponse("done")
