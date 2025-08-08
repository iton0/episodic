from typing import override
from django.db import models


class Person(models.Model):
    # NOTE: tmdb provides an id from results
    tmdb_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=250)
    picture_url = models.CharField(max_length=500, blank=True, null=True)

    @override
    def __str__(self):
        return self.name


class Genre(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=150)

    @override
    def __str__(self):
        return self.name


class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=500)
    # NOTE: storing as string is most suitable for PWA caching functionality
    poster_url = models.CharField(max_length=500, blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    watch_date = models.DateField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name="movies")

    @override
    def __str__(self):
        return self.title


class MovieCredit(models.Model):
    tmdb_credit_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    character = models.CharField(max_length=200, blank=True)
    job = models.CharField(max_length=200, blank=True)

    @override
    def __str__(self):
        if self.job == "actor":
            return f"{self.person.name} as {self.character} in {self.movie.title}"
        else:
            return f"{self.person.name} ({self.job}) for {self.movie.title}"


class Show(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=500)
    poster_url = models.CharField(max_length=500, blank=True, null=True)
    first_air_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name="shows")

    @override
    def __str__(self):
        return self.title


class Season(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="seasons")
    tmdb_id = models.IntegerField(unique=True)
    number = models.IntegerField(default=0)
    title = models.CharField(max_length=200)

    @override
    def __str__(self):
        return self.title


class Episode(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name="episodes"
    )
    first_air_date = models.DateTimeField(null=True, blank=True)
    watch_date = models.DateField(null=True, blank=True)
    number = models.IntegerField(default=0)
    title = models.CharField(max_length=500)
    poster_url = models.CharField(max_length=500, blank=True, null=True)
    runtime = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    @override
    def __str__(self):
        return self.title


class EpisodeCredit(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    character = models.CharField(max_length=200, blank=True)
    job = models.CharField(max_length=200, blank=True)
    tmdb_credit_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )

    @override
    def __str__(self):
        show_title = self.episode.season.show.title

        if self.job == "actor":
            return f"{self.person.name} as {self.character} in {show_title}: {self.episode.title}"
        else:
            return f"{self.person.name} ({self.job}) for {show_title}: {self.episode.title}"
