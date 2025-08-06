from django.db import models


# Create your models here.
# TODO: check what tmdb passes as acceptable parameters for movie and show
class Movie(models.Model):
    # tmdb provides:
    #    title ✓
    #    poster ✓
    #    runtime
    #    release date
    #    director
    #    actors
    #    genre
    # episodic provides:
    #   watch date
    pass


class Show(models.Model):
    # tmdb provides:
    #    title
    #    poster
    #    description
    #    release date
    #    director
    #    actors
    #    genre
    # episodic provides:
    #    completed?
    pass


class Season(models.Model):
    # tmdb provides:
    #   seasons/season numbers
    #   number of episodes (not the episodes themselves)
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)

    pass


class Episode(models.Model):
    # tmdb provides:
    #    title
    #    description
    #    release date
    #    runtime
    #    director
    #    actors
    # episodic:
    #   watch date
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE)

    pass
