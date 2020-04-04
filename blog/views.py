from django.shortcuts import render
# . means from the models.py in the current package
from .models import Post

# from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


#    return HttpResponse("<h1>Blog About</h1>")
