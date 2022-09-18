from django.db import models
from django.contrib.auth import get_user_model


class DMRoom(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="dm_author")
    addressee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="dm_addressee")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.addressee)