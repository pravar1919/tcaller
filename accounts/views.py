from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from rest_framework import generics
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAdminUser


class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        phone = data['phone']
        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if CustomUser.objects.filter(phone=phone).exists():
                return Response({'error': 'Phone already exists'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must be at least 6 characters'})
                else:
                    user = CustomUser.objects.create_user(
                        phone=phone, email=email, password=password, name=name)

                    user.save()
                    return Response({'success': 'User created successfully'})
        else:
            return Response({'error': 'Passwords do not match'})


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
