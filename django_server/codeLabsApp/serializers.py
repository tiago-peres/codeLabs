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
    user = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=MyUser.objects.all())],
            min_length=5,
            max_length=20
            )
    date = serializers.DateTimeField(
            required=True,
            input_formats=['%d-%m-%Y']
    )

    class Meta:
        model = MyUser
        fields = ('user', 'date')

    #def create_user(self, validated_data):
    #    user = MyUser.objects.create_atrisk(validated_data['user'], validated_data['date'])
    #    return user

