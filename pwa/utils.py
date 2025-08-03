import tmdbsimple as tmdb
from django.conf import settings


def search_movies(query):
    tmdb.API_KEY = settings.TMDB_API_KEY
    search = tmdb.Search()
    response = search.movie(query=query)

    # Process the results to get a clean list of movies
    movies = []
    for s in search.results:
        movies.append(
            {
                "id": s["id"],
                "title": s["title"],
                "poster_path": (
                    f"https://image.tmdb.org/t/p/w500{s['poster_path']}"
                    if s["poster_path"]
                    else None
                ),
                "release_date": s["release_date"],
            }
        )
    return movies
