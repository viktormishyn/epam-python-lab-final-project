from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(self, email, username, password, staff=False, admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not username:
            raise ValueError("Users must have a username")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          staff=staff, admin=admin)
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, email, username, password):
        user = self.create_user(email, username, password, staff=True)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email, username, password, staff=True, admin=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)  # manager, non superuser
    admin = models.BooleanField(default=False)  # superuser
    # TODO - create email verification
    confirmed = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # email and password are required by default

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_username(self):
        return self.username

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     # extend extra data
