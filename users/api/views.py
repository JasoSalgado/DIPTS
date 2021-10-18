# blog/users/api/views.py
# Rest framework modules
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# my modules
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from users.models import User

class RegisterView(APIView):
    """
    Register new users
    """
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    """
    Users must be authenticated
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # It will use all data from UserSerializer
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


    def put(self, request):
        # User can modify info
        # It returns data from user that is making the request
        user = User.objects.get(id=request.user.id) 
        # user = user data
        # request.data = new user data
        serializer = UserUpdateSerializer(user, request.data)
        # Validate info
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)