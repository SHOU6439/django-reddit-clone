from chat.models import DMRoom, DMInvite
from users.models.user import User

def ignore_dm_invite_action(dm_invite: DMInvite, author: User, addressee: User):
    dm_invite.ignore = True
    if not DMRoom.objects.filter(author=author, addressee=addressee):
        dm_invite.delete()
        DMRoom.objects.filter(
            author=addressee,
            addressee=author
        ).delete()