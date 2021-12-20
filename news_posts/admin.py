from django.contrib import admin
from .models import NewsPosts, Comment
# Register your models here.

admin.site.register(NewsPosts)
admin.site.register(Comment)