from django.contrib import admin
from reviews.models import Profile, Tag, Movie, Review, Genre, Director, Actor

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    model = Director

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    model = Actor

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    model = Movie

    list_display = (
        "id",
        "title",
        "release_date",
        "slug",
    )
    list_filter = (
        "title",
        "director",
        "cast",
        "release_date",
    )
    list_editable = (
        "title",
        "release_date",
        "slug",
    )
    search_fields = (
        "title",
        "release_date",
        "director",
        "cast",
        "slug",
        "tags",
        "genre",
        "watched",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "release_date",
        )
    }
    date_hierarchy = "release_date"
    save_on_top = True

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review

    list_display = (
        "id",
        "title",
        "movie",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "movie",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "movie",
        "slug",
        "body",
        "tags",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "movie",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True