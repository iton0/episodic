from django.shortcuts import render
from django.http import HttpResponse

from pwa.utils import search_movies


# Create your views here.
def index(request):
    return HttpResponse("Hello from pwa index.")


def movie_search(request):
    query = request.GET.get("query")
    movies = []
    if query:
        movies = search_movies(query)

    context = {"movies": movies, "query": query}
    return render(request, "pwa/search.html", context)
