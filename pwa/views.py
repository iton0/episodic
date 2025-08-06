from django.shortcuts import render
from django.http import HttpResponse

from pwa.utils import multi_search


# Create your views here.
def index(request):
    return render(request, "pwa/index.html")


def search(request):
    query = request.GET.get("query")
    medias = []
    if query:
        medias = multi_search(query)

    context = {"medias": medias, "query": query}
    return render(request, "pwa/search.html", context)
