from django.db import models


class Game(models.Model):
    RPG = 'RPG'
    STR = 'Strategy'
    ACT = 'Action'

    GENRES = (
        (RPG, 'RPG'),
        (STR, 'Strategy'),
        (ACT, 'Action'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    genre = models.CharField(max_length=20, choices=GENRES, null=True)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.name
