from django.shortcuts import render
from blogpost.models import BlogPost

def home(request):
    posts = BlogPost.objects.order_by('-updated_at')

    choosen = []

    for post in posts:
        if(len(choosen) < 8):
            choosen.append(post)
        else:
            break

    for post in choosen:
        print(post.title)

    data = {
        "newest" : choosen
    }
    return render(request, 'index.html', data)