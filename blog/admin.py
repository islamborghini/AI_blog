from django.contrib import admin
from .models import Post
# Register your models here.

#register Post db in the admin page
admin.site.register(Post)
