from django.db import models

# TODO: how do we refernce from tmdb if values update from the api


# Create your models here.
class Person(models.Model):
    name = models.CharField()
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


# TODO: check what tmdb passes as acceptable parameters for movie and show
class Movie(models.Model):
    title = models.CharField()
    poster = None  # TODO: how to store posters especially with PWA functionality
    runtime = models.DurationField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    directors = models.ManyToManyField(
        Person, blank=True, related_name="directed_movies"
    )
    actors = models.ManyToManyField(Person, blank=True, related_name="acted_in_movies")
    genre = models.ManyToManyField(Genre, blank=True)
    watch_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Show(models.Model):
    # tmdb provides:
    #    title
    #    poster
    #    description
    #    release date
    #    directors
    #    actors
    #    genre
    title = None
    poster = None
    release_date = None
    description = None
    directors = None
    actors = None
    genre = None


class Season(models.Model):
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)

    # TODO: how do you represent specific order for seasons and episodes


class Episode(models.Model):
    # episodic provides:
    #    completed? TODO: this can be completed or up to date with current
    #    episodes
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE)
    release_date = models.DateTimeField(null=True, blank=True)
    watch_date = models.DateField(null=True, blank=True)
    number = models.IntegerField(default=0)
    title = None
    poster = None
    runtime = None
    description = None
    directors = None
    actors = None
    completion = None
