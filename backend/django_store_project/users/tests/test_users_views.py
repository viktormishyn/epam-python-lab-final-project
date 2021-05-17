from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class UserCreateTests(APITestCase):

    def test_post_user(self):
        url = reverse('create_user')

        # email is not provided
        response = self.client.post(
            url, data={'username': 'user', 'password': 'password'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # not valid email
        response = self.client.post(
            url, data={'email': 'user', 'username': 'user', 'password': 'password'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # not valid username
        response = self.client.post(
            url, data={'email': 'user@user.com', 'username': 111, 'password': ''})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # in order to create new user email, username and password should be provided
        data = {'email': 'user@user.com',
                'username': 'user', 'password': 'password'}
        url = reverse('create_user')
        response = self.client.post(url, data=data, forman='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class JwtTokenTests(APITestCase):
    def setUp(self):
        # create regular user
        self.user = User.objects.create_user(
            'user@user.com', 'username', 'password')
        self.user.save()

    def tearDown(self):
        self.client.logout()
        self.user.delete()

    def test_obtain_blacklist_jwt_token(self):
        # obtain jwt token pair
        response = self.client.post(
            reverse('token_obtain_pair'), data={'email': 'user@user.com', 'password': 'password'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        refresh_token = response.data['refresh']
        # get new access token using refresh
        response = self.client.post(reverse('token_refresh'), data={
                                    'refresh': refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # blacklist refresh_token
        response = self.client.post(reverse('blacklist'), data={
                                    'refresh_token': refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # try to get new access token using blacklisted token
        response = self.client.post(reverse('token_refresh'), data={
            'refresh': refresh_token})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # try to blacklist old refresh token again
        response = self.client.post(reverse('blacklist'), data={
            'refresh_token': refresh_token})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
