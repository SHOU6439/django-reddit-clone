from django.contrib.auth import get_user_model
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Communities(models.Model):
    name = models.CharField(max_length=21, unique=True)
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='admin')
    member = models.ManyToManyField(get_user_model(), related_name='member')

    community_type = models.CharField(
        choices = (
            ('0','public'),
            ('1','restrict'),
            ('2','private'),
        ),
        max_length=20,
    )

    photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
    thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(80, 80)], format='JPEG', options={'quality': 60})

    is_nsfw = models.BooleanField(null=True, blank=True)

    latest_posted_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'communities'

