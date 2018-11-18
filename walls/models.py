import datetime
import os

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save


from walls.utils import unique_slug_generator, upload_image

INACTIVE = False
ACTIVE = True
STATUS = (
    (INACTIVE, ('Inactive')),
    (ACTIVE, ('Active')),
)


class Categories(models.Model):
    """Model that defines the Table structure of categories table

    Arguments:
        models {class} -- Base class for model
    """

    title = models.CharField(("Category Name"), unique=True, max_length=30)
    image = models.ImageField(("Category Image"), upload_to=upload_image)
    active = models.BooleanField(default=1, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def upload_to(self):
        return 'wallpaper_media/categories/'


class Wallpapers(models.Model):
    """Model that defines the Table structure of categories table

    Arguments:
        models {class} -- Base class for model
    """

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_image)
    category = models.ForeignKey(
        Categories, on_delete=models.DO_NOTHING, related_name='category')
    tags = models.TextField(null=True, blank=True)
    location = models.CharField(null=True, blank=True, max_length=50)
    description = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    uploader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    slug = models.SlugField(max_length=60, unique=True)
    active = models.BooleanField(default=1, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def upload_to(self):
        return 'wallpaper_media/wallpapers/'

    def get_tags(self):
        return [one.strip() for one in self.tags.split(',')]


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance, instance.title, instance.slug)


pre_save.connect(slug_save, sender=Wallpapers)


class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    description = models.TextField(max_length=200)
    active = models.BooleanField(default=1, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class TeamMembers(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.IntegerField()
    position = models.CharField(max_length=30)
    skills = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to=upload_image)
    github = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    instagram = models.URLField(null=True)
    twitter = models.URLField(null=True)
    facebook = models.URLField(null=True)
    active = models.BooleanField(default=1, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def upload_to(self):
        return 'site_media/teammember/'

    def get_name(self):
        return self.first_name + ' ' + self.last_name
