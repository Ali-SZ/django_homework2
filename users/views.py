from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class RegisterApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        })
        
class LoginApiView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        user = authenticate(phone = phone, passsword = password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key
            })
        else:
            return Response({
                'error': 'Invalid credentials'
            })
        
        
        