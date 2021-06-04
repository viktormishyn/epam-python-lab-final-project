from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Game, Genre

User = get_user_model()


class TestPermissions(APITestCase):
    def setUp(self):
        # create auth user
        self.user = User.objects.create_user(
            'user@user.com', 'user', 'password')
        self.user.save()
        # create another user
        self.user2 = User.objects.create_user(
            'user2@user.com', 'user2', 'password')
        self.user2.save()
        # create manager user
        self.manager = User.objects.create_user(
            'manager@manager.com', 'manager', 'password')
        self.manager.is_staff = True
        self.manager.save()
        # create admin user
        self.admin = User.objects.create_superuser(
            'admin@admin.com', 'admin', 'password')
        self.admin.save()
        # create genre, game models
        self.test_genre = Genre.objects.create(name='TestGenre')
        self.test_game = Game.objects.create(name='TestGame', price=100)  # id=1

    def tearDown(self):
        self.client.logout()
        self.user.delete()
        self.user2.delete()
        self.manager.delete()
        self.admin.delete()
        self.test_game.delete()
        self.test_genre.delete()

    def test_crud_genres_permissions(self):
        # anybody can see genres
        url = reverse('genres')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # only admin user is allowed to put, post or delete genres

        data = {'name': 'Genre1'}
        url = reverse('genres')
        # guest
        response = self.client.post(url, data=data, forman='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # auth user
        self.client.login(email='user@user.com', password='password')
        response = self.client.post(url, data=data, forman='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()
        # manager
        self.client.login(email='manager@manager.com', password='password')
        response = self.client.post(url, data=data, forman='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()
        # admin
        self.client.login(email='admin@admin.com', password='password')
        response = self.client.post(url, data=data, forman='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    # view game: admin, manager, auth user, guest
    def test_get_games_permissions(self):
        # guest
        url = reverse('games')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # auth user
        self.client.login(email='user@user.com', password='password')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
        # manager
        self.client.login(email='manager@manager.com', password='password')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
        # admin
        self.client.login(email='admin@admin.com', password='password')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    # crud game: admin, manager
    def test_post_put_delete_games_permissions(self):

        data = {'name': 'Game', 'description': 'description',
                'price': '100', 'genre': 'TestGenre'}

        # guest
        url = reverse('games')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # auth user
        self.client.login(email='user@user.com', password='password')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        # manager
        self.client.login(email='manager@manager.com', password='password')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.client.get(url, format='json').data[1]['name'], 'Game')
        response = self.client.put(reverse('game', kwargs={'id': '2'}), data={
                                   'name': 'NewName', 'description': 'new description'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.get(reverse('game', kwargs={'id': '2'})).data['name'], 'NewName')
        response = self.client.delete(reverse('game', kwargs={'id': '2'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.client.get(reverse('game', kwargs={'id': '2'})).status_code, status.HTTP_404_NOT_FOUND)
        self.client.logout()

        # admin
        self.client.login(email='admin@admin.com', password='password')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.client.get(url, format='json').data[1]['name'], 'Game')
        response = self.client.put(reverse('game', kwargs={'id': '3'}), data={
                                   'name': 'NewName', 'description': 'new description'})  # the id now should be 3 !!!!
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.get(reverse('game', kwargs={'id': '3'})).data['name'], 'NewName')
        response = self.client.delete(reverse('game', kwargs={'id': '3'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.client.get(reverse('game', kwargs={'id': '3'})).status_code, status.HTTP_404_NOT_FOUND)
        self.client.logout()

    # crud own comment: admin, manager, user; guest can not leave comments
    def test_post_put_delete_comments(self):
        response = self.client.get(reverse('posts-detail', kwargs={'pk': '1'}), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # guests are not allowed to post comments
        url = reverse('posts-list')
        data = {'game_id': '1', 'content': 'Post content'}
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # auth user is allowed to post comments
        self.client.login(email='user@user.com', password='password')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(reverse('posts-detail', kwargs={'pk': '1'}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['game'], 1)
        self.assertEqual(response.data['author']['username'], 'user')
        self.assertEqual(response.data['content'], 'Post content')
        self.assertEqual(response.data['edited'], False)
        self.client.logout()

        # comments can only be modified or deleted by the author, admin or manager
        response = self.client.get(reverse('posts-detail', kwargs={'pk': '1'}), format='json')
        self.assertEqual(response.data['author']['username'], 'user')
        self.assertEqual(response.data['content'], 'Post content')
        response = self.client.put(
            reverse('posts-detail', kwargs={'pk': '1'}), data={'content': 'modified content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.delete(
            reverse('posts-detail', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # login user2
        self.client.login(email='user2@user.com', password='password')
        response = self.client.put(
            reverse('posts-detail', kwargs={'pk': '1'}), data={'content': 'modified content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.delete(
            reverse('posts-detail', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        # login manager
        self.client.login(email='manager@manager.com', password='password')
        response = self.client.put(
            reverse('posts-detail', kwargs={'pk': '1'}), data={'content': 'modified content'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(reverse('posts-detail', kwargs={'pk': '1'}), format='json')
        self.assertEqual(response.data['author']['username'], 'user')
        self.assertEqual(response.data['content'], 'modified content')
        self.assertEqual(response.data['edited'], True)

        # login author again
        self.client.login(email='user@user.com', password='password')
        response = self.client.delete(
            reverse('posts-detail', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.logout()

    def test_orders_permissions(self):
        # TODO guests should be able to make orders!!
        # for now - temporary permission class IsAuthenticated

        url = reverse('orders')

        # guest
        response = self.client.get(reverse('orders'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # user
        self.client.login(email='user@user.com', password='password')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['get_items']), 0)

        response = self.client.post(url, data={'id': 1, 'qty': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(url)
        self.assertEqual(len(response.data['get_items']), 1)

        self.assertEqual(response.data['user'], 1)
        self.assertEqual(response.data['ordered'], False)
        self.assertEqual(response.data['get_items'][0]['game']['name'], 'TestGame')
        self.assertEqual(response.data['get_items'][0]['qty'], 5)
        self.assertEqual(response.data['get_total'], 500)

        response = self.client.put(url, data={'id': 1, 'qty': 4})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(url)
        self.assertEqual(response.data['user'], 1)
        self.assertEqual(response.data['ordered'], False)
        self.assertEqual(response.data['get_items'][0]['game']['name'], 'TestGame')
        self.assertEqual(response.data['get_items'][0]['qty'], 4)
        self.assertEqual(response.data['get_total'], 400)

        response = self.client.post(reverse('checkout'), data={
                                    'first_name': 'John', 'last_name': 'Smith', 'email': 'john_smith@gmail.com',
                                    'phone': '+380631111111', 'payment_type': 'Privat24', 'comments': 'comments'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(url)
        self.assertEqual(len(response.data['get_items']), 0)
