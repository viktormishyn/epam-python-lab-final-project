from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from store.models import Genre, Game

User = get_user_model()


class OrderViewTests(APITestCase):

    def setUp(self):
        # create regular users
        self.user1 = User.objects.create_user(
            'user1@user.com', 'user1', 'password1')
        self.user2 = User.objects.create_user(
            'user2@user.com', 'user2', 'password2')
        self.user1.save()
        self.user2.save()
        # create games
        self.genre = Genre.objects.create(name='Genre')
        self.genre.save()
        self.game1 = Game.objects.create(name='Game1', description='description', price='100', genre=self.genre)
        self.game2 = Game.objects.create(name='Game2', description='description', price='200', genre=self.genre)
        self.game1.save()
        self.game2.save()

    def tearDown(self):
        self.client.logout()
        self.user1.delete()
        self.user2.delete()
        self.game1.delete()
        self.game2.delete()
        self.genre.delete()

    def test_add_item_to_order(self):
        # anonymous user can not get orders or post order items
        item1 = {'id': 1, 'qty': '2'}
        item2 = {'id': 2, 'qty': '4'}
        item3 = {'id': 1, 'qty': '1'}
        url = reverse('orders')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.post(url, data=item1, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # user1
        self.client.login(email='user1@user.com', password='password1')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['get_items']), 0)
        # post 2 order items
        response = self.client.post(url, data=item1, format='json')
        response = self.client.post(url, data=item2, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['user'], 1)
        self.assertEqual(len(response.data['get_items']), 2)
        self.assertEqual(response.data['get_items'][1]['game']['name'], 'Game2')
        self.assertEqual(response.data['get_total'], 1000)
        self.client.logout()

        # user2
        self.client.login(email='user2@user.com', password='password2')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['get_items']), 0)
        # post 2 order items
        response = self.client.post(url, data=item3, format='json')
        response = self.client.post(url, data=item2, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['user'], 2)
        self.assertEqual(len(response.data['get_items']), 2)
        self.assertEqual(response.data['get_items'][0]['game']['name'], 'Game1')
        self.assertEqual(response.data['get_total'], 900)
        # if OrderItem with the game already exists in Order
        response = self.client.post(url, data=item2, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.client.logout()

    def test_delete_item_from_order(self):
        item1 = {'id': 1, 'qty': '2'}
        item2 = {'id': 2, 'qty': '4'}
        url = reverse('orders')

        self.client.login(email='user1@user.com', password='password1')
        # post 2 order items
        response = self.client.post(url, data=item1, format='json')
        response = self.client.post(url, data=item2, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['user'], 1)
        self.assertEqual(len(response.data['get_items']), 2)
        # delete 1st item
        response = self.client.delete(url, data={'id': 1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url)
        self.assertEqual(len(response.data['get_items']), 1)
        self.assertEqual(response.data['get_items'][0]['game']['name'], 'Game2')
        self.client.logout()

    def test_update_item_from_order(self):
        item1 = {'id': 1, 'qty': '2'}
        item2 = {'id': 2, 'qty': '4'}
        url = reverse('orders')

        self.client.login(email='user1@user.com', password='password1')
        # post 2 order items
        response = self.client.post(url, data=item1, format='json')
        response = self.client.post(url, data=item2, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['get_items'][0]['qty'], 2)
        # update 1st item
        response = self.client.put(url, data={'id': 1, 'qty': 9})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['get_items'][0]['qty'], 9)
