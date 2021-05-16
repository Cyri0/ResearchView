from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import home
from blogpost.views import blog, post
from img_uploader.views import image_embed 

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/<str:category>/', blog, name='blog'),
    path('post/<int:id>/', post, name='post'),
    path('images/', image_embed, name='images'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)