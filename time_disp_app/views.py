from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
    
def index(request):
    context = {
        # "name": "Noelle",
        # "favorite_color": "turquoise",
        # "pets": ["Bruce", "Fitz", "Georgie"]
        "time": strftime("%m-%d, %Y %H:%M %p", gmtime())
    }
    return render(request, "index.html", context)