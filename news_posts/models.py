from django.db import models
from users.models import User
from communities.models import Communities

class NewsPosts(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=64)
    content = models.TextField(max_length=512)
    vote = models.IntegerField(default=0)
    community = models.ForeignKey(Communities, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'news_posts'