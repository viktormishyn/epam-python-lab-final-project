from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserAccountTests(TestCase):

    def test_new_superuser(self):
        super_user = User.objects.create_superuser(
            'testuser@super.com', 'username', 'password')
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.username, 'username')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), 'username')

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='testuser@super.com', username='username', password='password', is_superuser=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='testuser@super.com', username='username', password='password', is_staff=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='', username='username', password='password')
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='testuser@super.com', username='', password='password')
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='testuser@super.com', username='username', password='')

    def test_new_user(self):
        user = User.objects.create_user(
            'testuser@user.com', 'username', 'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertEqual(user.username, 'username')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        # self.assertFalse(user.is_active) # TODO
        self.assertEqual(str(user), 'username')
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email='', username='username', password='password')
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email='testuser@user.com', username='', password='password')
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email='testuser@user.com', username='username', password='')
