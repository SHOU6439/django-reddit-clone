from chat.models import DMRoom, DMInvite, DirectMessage
from users.models.user import User
from django.contrib.auth import get_user_model

def accept_dm_invite_action(addressee_pk: int, author: User, dm_invite: DMInvite):
    User = get_user_model()
    addressee = User.objects.get(id=addressee_pk)
    dm_invite.accept = True
    dm_invite.delete()
    if not DMRoom.objects.filter(author=author, addressee=addressee):
        DMRoom.objects.create(author=author, addressee=addressee)
        addressee_room_messages = DirectMessage.objects.filter(
            room=DMRoom.objects.get(author=addressee, addressee=author),
        )
        if addressee_room_messages:
            message_storage = []
            for message in addressee_room_messages:
                message_storage.append(DirectMessage(
                    room=DMRoom.objects.get(author=author, addressee=addressee),
                    sender=message.sender,
                    content=message.content,
                    created_at=message.created_at,
                ))
            DirectMessage.objects.bulk_create(
                message_storage
            )
