from django.db import models
from .user import User

class bookmarked_posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("news_posts.NewsPosts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username) + "が" + str(self.post.title) + "を保存しました"