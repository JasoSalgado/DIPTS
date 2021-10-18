# blog/users/api/serializers.py
# Rest framework modules
from rest_framework import serializers
# My modules
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Fields to use
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
    
    def create(self, validated_data):
        """
        Encode password
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    """
    User can see: id, email, username, first_name, last_name
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']

class UserUpdateSerializer(serializers.ModelSerializer):
    """
    User can modify first_name and last_name only
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name']