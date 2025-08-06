import tmdbsimple as tmdb
from django.conf import settings


def multi_search(query):
    # NOTE: the fields for movies and tv shows are not the same
    # TODO: query all the information wanted for movies/tv. consult with api
    # reference for both movies, tv, and mutli https://developer.themoviedb.org/reference/intro/getting-started
    import tmdbsimple as tmdb
    from django.conf import settings

    search = tmdb.Search()
    tmdb.API_KEY = settings.TMDB_API_KEY
    response = search.multi(query=query)

    results = []
    for s in search.results:
        if s.get("media_type") in ["movie", "tv"]:
            item = {
                "id": s["id"],
                "poster_path": (
                    f"https://image.tmdb.org/t/p/w500{s['poster_path']}"
                    if s.get("poster_path")
                    else None
                ),
            }

            if s["media_type"] == "movie":
                item["title"] = s.get("title", "No Title")
                item["release_date"] = s.get("release_date", "Unknown Release Date")
            elif s["media_type"] == "tv":
                item["title"] = s.get("name", "No Title")
                # TV shows have 'first_air_date' instead of 'release_date'
                item["release_date"] = s.get("first_air_date", "Unknown Release Date")

            results.append(item)

    return results
