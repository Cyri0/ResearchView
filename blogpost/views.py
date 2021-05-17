from django.shortcuts import render
from .models import BlogPost

def blog(request, category):
    posts = BlogPost.objects.filter(category=category)

    data = {
        "category":category,
        "posts":posts,
    }

    return render(request, 'blog.html', data)

def post(request, id):
    posts = BlogPost.objects.filter(id = id)

    data = {
        "post":posts[0],
        "hero":str(posts[0].hero_image),
    }

    return render(request, 'post.html', data)

def blog_by_tag(request, tag):
    all_posts = BlogPost.objects.all()
    posts = []
    for post in all_posts:
        for actual_tag in post.tags.all():
            if actual_tag.name == tag:
                posts.append(post)

    data = {
        "category":tag,
        "posts":posts,
    }

    return render(request, 'blog.html', data)