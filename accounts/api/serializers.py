from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator

from ..models import CustomUser



class UserRegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    
    # password = serializers.CharField(
    #     max_length=68, min_length=6)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['email'], 
                                        validated_data['username'], 
                                        validated_data['password'])
        return user

    # def validate_password(self, value: str):
    #     """
    #     Hash value passed by user.

    #     :param value: password of a user
    #     :return: a hashed version of the password
    #     """
    #     return make_password(value)
