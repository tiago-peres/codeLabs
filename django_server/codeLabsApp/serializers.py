from django.core.validators import EmailValidator
from rest_framework.serializers import ModelSerializer
from codeLabsApp.models import MyUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
'''
FROM: USER APP
'''
class MyUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=MyUser.objects.all())],
            min_length=5,
            max_length=20
            ),
    password = serializers.CharField(
            required=True,
            max_length=256
            )
    
    class Meta:
        model = MyUser
        fields = ('username', 'password')
        
    def create(self, validated_data):
        password = make_password(validated_data['password'])
        user = MyUser.objects.create_user(validated_data['username'], password)
        return user

