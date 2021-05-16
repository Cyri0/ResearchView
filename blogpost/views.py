from django.shortcuts import render
from .models import BlogPost

def blog(request, category):
    posts = BlogPost.objects.filter(category=category)

    data = {
        "category":category,
        "posts":posts,
    }

    if(len(posts) == 0):
        pass #TODO

    return render(request, 'blog.html', data)

def post(request, id):
    posts = BlogPost.objects.filter(id = id)

    data = {
        "post":posts[0],
        "hero":str(posts[0].hero_image),
    }

    return render(request, 'post.html', data)
