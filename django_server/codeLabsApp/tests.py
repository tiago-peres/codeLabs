from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase
from rest_framework import status
# Create your tests here.

'''
FROM: USER APP
'''
# Yet to consider possible user registration errors
class MyUserTest(APITestCase):
    def setUp(self):
        # Create a user
        self.test_user = MyUser.objects._create_user('tiagoperes', '28-05-2020')

        # URL for creating user
        self.create_url = reverse('user-create')

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'user': 'tiagoperes',
            'date': '28-05-2020'
        }

        response = self.client.post(self.create_url , data, format='json')

        # Make sure we have two users in the database
        self.assertEqual(MyUser.objects.count(), 2)
        # Return 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Return the username and email upon successful creation
        self.assertEqual(response.data['user'], data['user'])
        self.assertEqual(response.data['date'], data['date'])

    #TODO test creating user with too long username, with preexisting username, with older / earlier date than today...

