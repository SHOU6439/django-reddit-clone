from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey
from users.models import User
from config import settings

# Create your models here.
class Communities(models.Model):
    name = models.CharField(max_length=21)
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='admin')
    member = models.ManyToManyField(get_user_model(), related_name='member')
    community_type = ('public', 'restrict', 'private')
    is_nsfw = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'communities'



