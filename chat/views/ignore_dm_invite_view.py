from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from chat.models import DMRoom, DMInvite
from django.contrib.auth import get_user_model
from django.shortcuts import redirect





class IgnoreDMInviteView(LoginRequiredMixin, generic.View):
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
        dm_invite.ignore = True
        if not DMRoom.objects.filter(author=author, addressee=addressee):
            dm_invite.delete()
            DMRoom.objects.filter(
                author=addressee,
                addressee=author
            ).delete()
        return redirect('chat:home')
