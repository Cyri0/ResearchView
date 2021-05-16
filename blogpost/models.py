from django.db import models
from datetime import date, datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
import json


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    CATEGORY_CHOICES = (
        ('music','zene'),
        ('book', 'könyv'),
        ('comic','képregény'),
        ('movie','film'),
        ('game','videojáték'),
        ('research','kutatás'),
    )
    title = models.CharField(max_length = 50)
    shortcontent = models.TextField(default="", max_length= 200)
    content = models.TextField(default="")
    category = models.CharField(max_length = 100, choices=CATEGORY_CHOICES, default='paint')
    
    hero_image = models.ImageField(upload_to='hero_images/', default = '')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.title + " ("+self.category+")"

    @property
    def date_is_changed(self):
        return self.created_at.strftime("%B%d%Y%H%M%S") != self.updated_at.strftime("%B%d%Y%H%M%S")
    
    @property
    def hero(self):
        return str(self.hero_image)



@receiver(post_save, sender=BlogPost)
def my_handler(sender, instance, **kwargs):
    now = datetime.now()
    current_time = now.strftime("%Y%m%d-%H%M%S")
    filename = str(instance.id)+"-"+str(current_time)
    save_data = {
        "title":str(instance.title),
        "datetime":now.strftime("%Y.%m.%d. - %H:%M:%S"),
        "category":str(instance.category),
        "short":str(instance.shortcontent),
        "content":str(instance.content)
    }
    f = open(os.getcwd()+"/saved_posts/{}.json".format(filename), "a")
    f.write(json.dumps(save_data, indent = 4))
    f.close()
