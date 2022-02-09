from django.db import models
from django.conf import settings
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _


from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField


# Create your models here.

class Posts(models.Model):
    title = models.CharField('Title', max_length = 256)
    cover_photo = models.ImageField('Cover Photo', upload_to = 'media/Posts')
    description = models.CharField('Description', max_length=256)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey('Category', on_delete = models.CASCADE, db_index = True, related_name = 'posts')
    content = models.ForeignKey('Content', on_delete = models.CASCADE, db_index = True, related_name = 'post')


class Content(models.Model):
    text = models.TextField('Text', max_length=256, blank=True, null=True)
    image = models.ImageField('Content Image', upload_to = 'media/Content', blank = True, null = True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Videos(models.Model):
    title = models.CharField('Title', max_length=256)
    video_link = models.URLField('Video link', max_length=300, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    title = models.CharField('Title', max_length=256)
