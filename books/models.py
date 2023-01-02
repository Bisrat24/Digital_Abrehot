from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class BGenre(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ISBN_number = models.CharField(max_length=100)
    src = models.CharField(max_length=200)
    cover_image = models.CharField(max_length=100)
    genre = models.ForeignKey(BGenre, on_delete=models.CASCADE)


class VGenre(models.Model):
    name = models.CharField(max_length=50)


class Video(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.CharField(max_length=100)
    src = models.CharField(max_length=200)
    genre = models.ForeignKey(VGenre, on_delete=models.CASCADE)


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, null=True, blank=True)
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
