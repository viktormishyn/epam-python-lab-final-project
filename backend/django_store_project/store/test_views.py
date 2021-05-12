from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from store.models import Game, Genre
from django.contrib.auth.models import User
from django_seed import Seed
from django.db.models import ProtectedError

seeder = Seed.seeder()
seeder.add_entity(Genre, 5)
seeder.add_entity(Game, 5)


class GamesTests(APITestCase):

    def test_get_games(self):
        url = reverse('games')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_games(self):
        # self.test_user = User.objects.create_user(
        #     username='user', password='password')
        self.test_genre = Genre.objects.create(name='Genre')
        data = {'name': 'Game', 'description': 'description',
                'price': '100', 'genre': 'Genre'}
        url = reverse('games')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_games(self):
        # seed db with 5 Game objects
        seeder.execute()

        # get request should return 5 items
        url = reverse('games')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

        # delete
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # get request should return 0 items
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class GameTests(APITestCase):

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
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(url)
        self.assertEqual(response.data['name'], 'New name')

    def test_delete_game(self):
        # seed db with 5 Game objects
        seeder.execute()
        url = reverse('game', kwargs={'id': '1'})

        # get 1st item
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # delete 1st item
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # try to get 1st item
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GenresTests(APITestCase):

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
