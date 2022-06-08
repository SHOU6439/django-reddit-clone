from django.db import models
from django.contrib.auth import get_user_model



class Notification(models.Model):
    title = models.CharField(max_length=128, unique=False)
    message = models.CharField(max_length=624, null=True, blank=True)
    destination = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="destination")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message