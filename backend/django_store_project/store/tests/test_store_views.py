from django.contrib.auth import get_user_model
from django.db.models import ProtectedError
from django.urls import reverse
from django_seed import Seed
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Game, Genre

seeder = Seed.seeder()
seeder.add_entity(Genre, 5)
seeder.add_entity(Game, 5)

User = get_user_model()


class GamesTests(APITestCase):

    def setUp(self):
        # create regular user
        self.user = User.objects.create_user(
            'user@user.com', 'username', 'password')
        self.user.save()
        # create manager
        self.manager = User.objects.create_user(
            'manager@manager.com', 'manager', 'password')
        self.manager.is_staff = True
        self.manager.save()
        # create admin
        self.admin = User.objects.create_superuser(
            'admin@admin.com', 'admin', 'password')
        self.admin.save()

    def tearDown(self):
        self.client.logout()
        self.user.delete()
        self.manager.delete()
        self.admin.delete()

    def test_get_games(self):
        # anybody is allowed see games without authentication
        url = reverse('games')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_games(self):
        self.test_genre = Genre.objects.create(name='Genre')
        data = {'name': 'Game', 'description': 'description',
                'price': '100', 'genre': 'Genre'}
        url = reverse('games')
        # anonymous users are not allowed to create games
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # regular users are not allowed to create games
        self.client.login(email='user@user.com', password='password')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()
        # staff is allowed to create games
        self.client.login(email='manager@manager.com', password='password')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()
        data = {'name': 'Game2', 'description': 'description',
                'price': '100', 'genre': 'Genre'}
        self.client.login(email='admin@admin.com', password='password')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    def test_delete_games(self):
        # seed db with 5 Game objects
        seeder.execute()

        # get request should return 5 items
        url = reverse('games')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

        # only superuser is allowed to use DELETE method
        # anonymous user
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # regular user
        self.client.login(email='user@user.com', password='password')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()
        # manager
        self.client.login(email='manager@manager.com', password='password')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()
        # admin
        self.client.login(email='admin@admin.com', password='password')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.logout()

        # get request should return 0 items
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class GameTests(APITestCase):

    def setUp(self):
        # create regular user
        self.user = User.objects.create_user(
            'user@user.com', 'username', 'password')
        self.user.save()
        # create manager
        self.manager = User.objects.create_user(
            'manager@manager.com', 'manager', 'password')
        self.manager.is_staff = True
        self.manager.save()
        # create admin
        self.admin = User.objects.create_superuser(
            'admin@admin.com', 'admin', 'password')
        self.admin.save()

    def tearDown(self):
        self.client.logout()
        self.user.delete()
        self.manager.delete()
        self.admin.delete()

    def test_get_game(self):
        # seed db with 5 Game objects
        seeder.execute()

        # get first object
        url = reverse('game', kwargs={'id': '1'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # try to get 6th object
        url = reverse('game', kwargs={'id': '6'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_game(self):
        # seed db with 5 Game objects
        seeder.execute()
        url = reverse('game', kwargs={'id': '1'})
        data = {'name': 'New name', 'description': 'New description'}

        # Only staff is allowed to update games
        # anonymous
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # regular user
        self.client.login(email='user@user.com', password='password')
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()
        # manager
        self.client.login(email='manager@manager.com', password='password')
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
        # admin
        self.client.login(email='admin@admin.com', password='password')
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_delete_game(self):
        # seed db with 5 Game objects
        seeder.execute()
        url = reverse('game', kwargs={'id': '1'})

        # get 1st item
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # delete 1st item
        # Only staff is allowed to delete games
        # anonymous
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # regular user
        self.client.login(email='user@user.com', password='password')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()
        # manager
        self.client.login(email='manager@manager.com', password='password')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.logout()

        # try to get 1st item
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GenresTests(APITestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(
            'admin@admin.com', 'username', 'password')
        self.admin.save()
        self.client.login(email='admin@admin.com', password='password')

    def tearDown(self):
        self.client.logout()
        self.admin.delete()

    def test_get_genres(self):
        url = reverse('genres')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_genres(self):
        data = {'name': 'Genre'}
        url = reverse('genres')
        response = self.client.post(url, data=data, forman='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_genres(self):
        # seed db with 5 Genre objects
        seeder.execute()

        # get request should return 5 items
        url = reverse('genres')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

        # try to delete all genres when there are game instances referencing genres
        with self.assertRaises(ProtectedError):
            response = self.client.delete(url)

        # delete all games
        self.client.delete(reverse('games'))

        # try to delete genres again
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # get request should return 0 items
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
