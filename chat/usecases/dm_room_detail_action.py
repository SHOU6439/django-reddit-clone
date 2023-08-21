from users.models.user import User
from chat.models import DMRoom, DMInvite, DirectMessage

def dm_room_detail_action(author: User, addressee: User, pk: int, context: dict):
    context['current_invite'] = DMInvite.objects.filter(invited_user=addressee, received_user=author)
    context['current_room'] = DMRoom.objects.get(id=pk)
    context['dm_list'] = DirectMessage.objects.filter(room=pk)
    context['dm_invites'] = DMInvite.objects.filter(received_user=author.id).order_by("-created_at")
    context['dm_rooms'] = DMRoom.objects.filter(author=author.id).order_by("-created_at")