from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from communities.models import Communities
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class NewsPosts(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=64, unique=False)
    content = models.TextField(max_length=512, null=True, blank=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
    post_photo = ImageSpecField(source='photo',processors=[ResizeToFill(1080,1080)],format='JPEG',options={'quality':60})
    vote = models.IntegerField(default=0)
    community = models.ForeignKey(Communities, on_delete=models.CASCADE, blank=True, null=True, related_name='community')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __init__(self):
    #     return self.vote

    class Meta:
        db_table = 'news_posts'

class Comment(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=512, null=True, blank=True)
    target = models. ForeignKey(NewsPosts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# class Replay(models.Model):
#     user = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE,
#     )
#     content = models.CharField(max_length=512, null=True, blank=True)
#     target = models. ForeignKey(Comment, on_delete=models.CASCADE)
#     mension = models.CharField(max_length=20, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)


class Vote(models.Model):
    voted_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    voted_post = models.ForeignKey(NewsPosts, on_delete=models.CASCADE, related_name="voted_post")
    flag = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.voted_user) + "が" + str(self.voted_post) + "を投票した"