from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # genre = models.CharField(max_length=20, choices=GENRES, null=True)
    genre = models.ForeignKey(
        Genre, to_field='name', on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.name
