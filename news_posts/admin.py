from django.contrib import admin
from .models import NewsPosts, Comment, Notification, Replay, Vote
# Register your models here.

admin.site.register(NewsPosts)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Notification)
admin.site.register(Replay)