from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    #passes the time now with current timezone
    date_posted = models.DateTimeField(default=timezone.now)

    #if the user is deleted, we delete a post
    author = models.ForeignKey(User, on_delete=models.CASCADE)