from rest_framework.viewsets import ModelViewSet
from .serializers import User, UserSerializers, LoginSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import login, logout
from django.core.cache import cache
from uuid import uuid1


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    @action(methods=["post"], detail=False, url_name="userlogin")
    def userlogin(self, request, *args, **kwargs):
        serializer = LoginSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, is_auth = serializer.authenticate_user(serializer.validated_data['email'],
                                                     serializer.validated_data['password'])

        """
            cache is set in redis server
            cache.set(user.email, "true")
        """

        if is_auth:
            uniq_id = str(uuid1())
            login(self.request, user)

            """
                this session also set in redis server
            """
            self.request.session[uniq_id] = (user.id, True)
            response = Response({"body": "login successfully"})
            response.set_cookie(key='userinfo', value=uniq_id, max_age=1000)
            return response
        else:
            return Response({"body": "Credential is not valid"})

    @action(methods=["get"], detail=False, url_name="userlogout")
    def userlogout(self, request, *args, **kwargs):
        cache.delete(self.request.user.email)
        logout(self.request)
        return Response({"body": "logout"})
