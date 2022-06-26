from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from reviews import models

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile

class GenreType(DjangoObjectType):
    class Meta:
        model = models.Genre

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag

class DirectorType(DjangoObjectType):
    class Meta:
        model = models.Director

class ActorType(DjangoObjectType):
    class Meta:
        model = models.Actor

class ProductionHouseType(DjangoObjectType):
    class Meta:
        model = models.ProductionHouse

class MovieType(DjangoObjectType):
    class Meta:
        model = models.Movie

class ReviewType(DjangoObjectType):
    class Meta:
        model = models.Movie
