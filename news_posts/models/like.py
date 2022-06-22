from django.db import models
from django.contrib.auth import get_user_model
from .news_posts import NewsPosts



class Like(models.Model):
    liked_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="liked_user")
    liked_post = models.ForeignKey(NewsPosts, on_delete=models.CASCADE, related_name="liked_post")
    is_liked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.liked_user) + "が" + str(self.liked_post) + "をいいねした"