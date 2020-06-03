from django.core.validators import EmailValidator
from rest_framework.serializers import ModelSerializer
from codeLabsApp.models import MyUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import datetime

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
            max_length=256,
            write_only=True
            )
    
    class Meta:
        model = MyUser
        fields = ('username', 'password')
        
    def create(self, validated_data):
        #password = make_password(validated_data['password'])
        user = MyUser.objects.create_user(validated_data['username'], validated_data['password'])
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data.pop('refresh', None) # remove refresh from the payload
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['user'] = self.user.username
        data['date'] = datetime.date.today()
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['iat'] = datetime.datetime.now()
        token['user'] = user.username
        token['date'] = str(datetime.date.today())

        return token