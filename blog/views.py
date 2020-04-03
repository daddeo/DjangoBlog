from django.shortcuts import render

# from django.http import HttpResponse

posts = [
    {
        "author": "John",
        "title": "Post 1",
        "content": "First post content",
        "posted": "April 1, 2020",
    },
    {
        "author": "Jane",
        "title": "Post 2",
        "content": "Second post content",
        "posted": "April 2, 2020",
    },
]

# Create your views here.
def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


#    return HttpResponse("<h1>Blog About</h1>")
