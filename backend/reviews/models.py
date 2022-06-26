from re import T
from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ProductionHouse(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=240, unique=True)
    release_date = models.DateField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    movie_synopsis = models.TextField(blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, blank=True)
    cast = models.ManyToManyField(Actor, blank=True)
    production_house = models.ManyToManyField(ProductionHouse, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    watched_date = models.DateField(blank=True, null=True)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        ordering = ["-publish_date"]
    
    title = models.CharField(max_length=255, unique=True)
    movie  = models.ForeignKey(Movie, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
