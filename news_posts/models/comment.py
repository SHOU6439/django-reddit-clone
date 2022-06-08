from django.db import models
from django.contrib.auth import get_user_model
from .news_posts import NewsPosts
from .replay import Replay

class Comment(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=512, null=True, blank=True)
    target = models.ForeignKey(NewsPosts, on_delete=models.CASCADE, related_name="comments")
    replay = models.ManyToManyField(Replay, related_name="replay")
    latest_replayed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content