from django.db import models
from PIL import Image
from django.core.files import File
from io import BytesIO
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'genres'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Game(models.Model):

    name = models.CharField(max_length=100, db_index=True, unique=True)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    genre = models.ForeignKey(
        Genre, to_field='name', on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to="images/", null=True)
    thumbnail = models.ImageField(upload_to="images/thumbnails/", null=True)
    added = models.DateTimeField(auto_now_add=True, null=True)
    # added_by = models.ForeignKey(User, on_delete=models.PROTECT)
    # updated = models.DateTimeField(auto_now=True, null=True)
    # updated_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'games'
        ordering = ('added',)

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def __str__(self):
        return self.name
