from django.db import models
from django.contrib.auth import get_user_model
from .news_posts import NewsPosts



class Vote(models.Model):
    voted_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    voted_post = models.ForeignKey(NewsPosts, on_delete=models.CASCADE, related_name="voted_post")
    flag = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.voted_user) + "が" + str(self.voted_post) + "を投票した"