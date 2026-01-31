from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

import logging

from accounts.serializers import RegisterSerializer

logger = logging.getLogger(__name__)



class RegisterAPIView(APIView):
    permission_classes = []
    def post(self, request):
        logger.info(f"Register attempt for username : {request.data.get('username')}")

        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f'User registered successfully : {user.username}')
            
            refresh = RefreshToken.for_user(user)
            logger.info(f"Tokens generated for user - {user.username} ")

            return Response({
                'user' : {
                    'username' : user.username,
                    'email' : user.email
                },
                'tokens' : {
                    'refresh' : str(refresh),
                    'access' : str(refresh.access_token)
                }
            }, status=status.HTTP_201_CREATED)
        
        else:
            logger.error(f"Registration failed : {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
