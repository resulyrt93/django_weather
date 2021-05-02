from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['POST'])
def register(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    same_username_user = User.objects.filter(username=username).first()
    if same_username_user is not None:
        raise APIException('Username using by someone else')

    if email is not None and password is not None and username is not None:
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
    else:
        raise APIException('Credentials are not correct!')

    serializer = UserSerializer(user)
    data = serializer.data

    token = Token.objects.create(user=user)
    data.update({'token': token.key})
    return Response(data)


class Logout(APIView):

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
