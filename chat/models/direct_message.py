from django.db import models
from django.contrib.auth import get_user_model
from .dm_room import DMRoom


class DirectMessage(models.Model):
    room = models.ForeignKey(DMRoom, on_delete=models.CASCADE, related_name="dm_room")
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="dm_sender")
    content = models.CharField(max_length=512, null=True, blank=True)
    recipient_message = models.ForeignKey("DirectMessage", on_delete=models.CASCADE, related_name="sender_message", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)