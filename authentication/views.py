from rest_framework import serializers, generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework import status, mixins
from rest_framework.response import Response

from authentication.serializers import LoginSerializer, RegisterSerializer
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        if not request.data.get('email') or not request.data.get('password'):
            return Response({"message": "Invalid operation. Please provide email and password"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)