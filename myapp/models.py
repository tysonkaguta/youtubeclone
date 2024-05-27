from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='channel-pictures/',height_field=None, width_field=None, max_length=100)


class Videos(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnails/',height_field=None, width_field=None, max_length=100)
    video_time = models.CharField(max_length=50)
    channel_picture = models.ImageField(upload_to='channel-pictures/',height_field=None, width_field=None, max_length=100)
    video_title = models.CharField(max_length=500)
    video_author = models.CharField(max_length=100)
    views = models.CharField(max_length=50) 
    period = models.CharField(max_length=100) 