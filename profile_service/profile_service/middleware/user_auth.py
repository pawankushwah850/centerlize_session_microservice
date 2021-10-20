from django.core.cache import cache
from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest

class UserAuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        self.session_id = request.COOKIES.get('userinfo',False)
        if not self.session_id:
            return HttpResponseBadRequest("user session uuid is missing")
        self.user_id, self.is_auth = request.session.get(self.session_id)
        response = self.get_response(request)

        return response
    
    def process_view(self,request, view_func, args, kwargs):
        
        if self.is_auth:
            request.user = self.user_id
            request.is_authenticated = self.is_auth
            

    def process_exception(self,request, exception):
        if not self.session_id or not self.is_auth:
            return HttpResponseBadRequest("Session id is missing")

