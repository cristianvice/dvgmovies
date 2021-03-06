import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from reviews import models

'''
NOTE:
in django 4.0 we dont have force_text

https://docs.djangoproject.com/en/4.0/ref/utils/#module-django.utils.encoding

instead change force_text to force_str

linux:

YOUR_VENV/lib/PYTHON_VERSION/site-packages/graphene_django/utils/utils.py

windows:

YOUR_VENV/lib/site-packages/graphene_django/utils/utils.py

from django.utils.encoding import force_text
to

from django.utils.encoding import force_str
'''
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
        model = models.Review

# Queries
class Query(graphene.ObjectType):
    all_reviews = graphene.List(ReviewType)
    all_movies = graphene.List(MovieType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    review_by_slug = graphene.Field(ReviewType, slug=graphene.String())
    movie_by_slug = graphene.Field(MovieType, slug=graphene.String())
    reviews_by_author = graphene.List(ReviewType, username=graphene.String())
    reviews_by_movie = graphene.List(ReviewType, movie=graphene.String())
    reviews_by_tag = graphene.List(ReviewType, tag=graphene.String())
    movies_by_genre = graphene.List(MovieType, genre=graphene.String())
    movies_by_cast = graphene.List(MovieType, cast=graphene.String())
    movies_by_director = graphene.List(MovieType, director=graphene.String())
    movies_by_production_house = graphene.List(MovieType, production_house=graphene.String())

    def resolve_all_reviews(root, info):
        return (
            models.Review.objects.prefetch_related("tags")
            .select_related("author")
            .select_related("movie")
            .all()
        )
    
    def resolve_all_movies(root, info):
        return (
            models.Movie.objects.prefetch_related("genre")
            .select_related("director")
            .all()
        )

    def resolve_author_by_username(root, info, username):
        return models.Profile.objects.select_related("user").get(
            user__username=username
        )

    def resolve_review_by_slug(root, info, slug):
        return (
            models.Review.objects.prefetch_related("tags")
            .select_related("author")
            .select_related("movie")
            .get(slug=slug)
        )

    def resolve_movie_by_slug(root, info, slug):
        return (
            models.Movie.objects.prefetch_related("genre")
            .select_related("director")
            .get(slug=slug)
        )

    def resolve_review_by_movie(root, info, movie):
        return models.Review.objects.select_related("movie").get(
            movie__title=movie  
        )

    def resolve_review_by_author(root, info, username):
        return (
            models.Review.objects.prefetch_related("tags")
            .select_related("author")
            .filter(author__user__username=username)
        )

    def resolve_movies_by_director(root, info, director):
        return (
            models.Movie.objects.prefetch_related("genre")
            .select_related("director")
            .filter(director__name__iexact=director)
        )

    def resolve_movies_by_production_house(root, info, production_house):
        return (
            models.Movie.objects.prefetch_related("genre")
            .select_related("director")
            .filter(production_house__name__iexact=production_house)
        )

    def resolve_reviews_by_tag(root, info, tag):
        return (
            models.Review.objects.prefetch_related("tags")
            .select_related("movie")
            .filter(tags__name__iexact=tag)
        )

    def resolve_movies_by_genre(root, info, genre):
        return (
            models.Movie.objects.prefetch_related("genre")
            .select_related("director")
            .filter(genre__name__iexact=genre)
        )
    
    def resolve_movies_by_cast(root, info, cast):
        return (
            models.Movie.objects.prefetch_related("genre")
            .select_related("director")
            .filter(cast__name__iexact=cast)
        )

schema = graphene.Schema(query=Query)  