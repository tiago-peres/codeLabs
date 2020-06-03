from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase
from codeLabsApp.models import MyUser
from rest_framework import status
# Create your tests here.

class MyUserTest(APITestCase):
    def setUp(self):
        # Create a user
        self.test_user = MyUser.objects.create_user('tiago', 'test')

        # URL for creating user
        self.create_url = reverse('user-create')

    def test_create_user(self):
        '''
        Ensure we can create a new user.
        '''
        data = {
            'username': 'tiagoperes',
            'password': 'test'
        }

        response = self.client.post(self.create_url , data, format='json')

        # Make sure we have two users in the database
        self.assertEqual(MyUser.objects.count(), 2)
        # Return 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Return the username and email upon successful creation
        self.assertEqual(response.data['username'], data['username'])
        self.assertFalse('password' in response.data)

    def test_create_user_with_short_password(self):
        '''
        Ensure we can't create a user with short password.
        '''
        data = {
            'username': 'tiagoperes',
            'password': 'eii'
        }

        response = self.client.post(self.create_url , data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(MyUser.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)


    def test_create_user_with_no_password(self):
        '''
        Ensure we can't create a user with no password.
        '''
        data = {
            'username': 'tiagoperes',
            'password': ''
        }

        response = self.client.post(self.create_url , data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(MyUser.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)


    def test_create_user_with_no_username(self):
        '''
        Ensure we can't create a user with no username.
        '''
        data = {
            'username': '',
            'password': 'test'
        }

        response = self.client.post(self.create_url , data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(MyUser.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    
    def test_create_user_with_too_long_username(self):
        '''
        Ensure we can't create a user with too long username.
        '''
        data = {
            'username': 'tiagoperes'*50,
            'password': 'test'
        }

        response = self.client.post(self.create_url , data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(MyUser.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)


    def test_create_user_with_preexisting_username(self):
        '''
        Ensure we can't create a user with preexisting username.
        '''
        data = {
            'username': 'testing',
            'password': 'test'
        }

        response = self.client.post(self.create_url , data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(MyUser.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

