from chat.models import DMRoom, DMInvite
from users.models import User

def chat_dm_home_list_action(user: User,context: dict):
    # TODO:のちにグループチャットを追加した際にグループチャットの一覧のコンテキストも渡す
    context['dm_invites'] = DMInvite.objects.filter(received_user=user.id).order_by("-created_at")
    context['dm_rooms'] = DMRoom.objects.filter(author=user.id).order_by("-created_at")