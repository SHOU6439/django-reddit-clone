from django.contrib import admin
from .models import User, bookmarked_posts
# Register your models here.
admin.site.register(User)
admin.site.register(bookmarked_posts)