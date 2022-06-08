from django.db import models
from django.contrib.auth import get_user_model
from .dm_room import DMRoom



class DMInvite(models.Model):
    room = models.ForeignKey(DMRoom, on_delete=models.CASCADE, related_name="invitation_room")
    invited_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="users_dm_invite")
    received_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="users_dm_receive")
    accept = models.BooleanField(default=False)
    ignore = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.invited_user) + "が" + str(self.received_user) + "をDMに招待しました"