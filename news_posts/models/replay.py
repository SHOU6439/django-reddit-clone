from django.db import models
from django.contrib.auth import get_user_model

class Replay(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=512, null=True, blank=True)
    # TODO:どのユーザーに向けてのReplayなのかを指定できるようにする。使用するフィールドも検討する。
    # mension = models.CharField(max_length=20, null=True, blank=True)
    target = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name="replay_target")
    created_at = models.DateTimeField(auto_now_add=True)