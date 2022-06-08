from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMRoom, DMInvite, DirectMessage
from django.contrib.auth import get_user_model
from django.shortcuts import redirect



class AcceptDMInviteView(LoginRequiredMixin, generic.View):
    model = DMInvite

    def get(self, request, *args, **kwargs):
        addressee_pk = self.kwargs['pk']
        User = get_user_model()
        author = User.objects.get(id=request.user.id)
        addressee = User.objects.get(id=addressee_pk)
        dm_invite = DMInvite.objects.filter(
            invited_user=addressee,
            received_user=author
        )
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
        author_room_pk = DMRoom.objects.get(
            author=author,
            addressee=addressee
        ).id
        return redirect('chat:dm_room_detail', pk=author_room_pk)
