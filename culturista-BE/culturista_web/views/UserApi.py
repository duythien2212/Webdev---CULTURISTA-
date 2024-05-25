from django.shortcuts import render, get_object_or_404,get_list_or_404

from ..models import User
from ..serializers import UserSerializer,LoginSerializer,RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework import viewsets,status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,DestroyAPIView,ListAPIView,GenericAPIView,CreateAPIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse,HttpResponseForbidden
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

# def check_login(token):
#         access_token = AccessToken(token)
#         # Kiểm tra tính hợp lệ của token
#         access_token.verify()
#         # Kiểm tra người dùng từ token
#         username = access_token.payload['username']
#         # Kiểm tra người dùng có tồn tại không
#         user = User.objects.get(pk=username)
#         # Kiểm tra trạng thái của người dùng
#         if user:
#             return True
#         else:
#             return False


def check_login(token):
    try:
        access_token = AccessToken(token)
        # Verify the validity of the token
        access_token.verify()
        # Get the user from the token
        username = access_token.payload['username']
        # Check if the user exists
        user = User.objects.get(pk=username)
        # Check the status of the user
        if user:
            return True
        else:
            return HttpResponseForbidden("User does not exist or is inactive.")
    except (User.DoesNotExist, AuthenticationFailed):
        return HttpResponseForbidden("Authentication failed. User not logged in.")

class GetAllUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginUser(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        access= refresh.access_token
        if  check_login(str(access)):
            return JsonResponse({
                    'refresh': str(refresh),
                    'access': str(access),
            })
        else:
            return JsonResponse({'error': 'Token is invalid'}, status=401)

    
def login_user(request):
    return render(request, 'login.html')
class RegisterUser(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

