from django.shortcuts import render
from .models import ImageUpload

def image_embed(request):
    imgs = ImageUpload.objects.all()
    data = {
        "images": imgs
    }
    return render(request, 'images.html', data)