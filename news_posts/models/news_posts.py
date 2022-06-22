from django.db import models
from django.contrib.auth import get_user_model
from communities.models import Communities
from imagekit.models import ImageSpecField
from users.models import bookmarked_posts


class NewsPosts(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    saved_user = models.ManyToManyField(get_user_model(),  related_name="saved_user", through='users.bookmarked_posts')
    title = models.CharField(max_length=64, unique=False)
    content = models.CharField(max_length=512, null=True, blank=True)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
    post_photo = ImageSpecField(source='photo', format='JPEG', options={'quality':60})
    like = models.IntegerField(default=0)
    community = models.ForeignKey(Communities, on_delete=models.CASCADE, blank=True, null=True, related_name='communities_post')
    latest_commented_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __init__(self):
    #     return self.vote
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'news_posts'
