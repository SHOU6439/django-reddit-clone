from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from chat.models import DirectMessage, DMRoom
from django.db.models import Model
from django.shortcuts import get_object_or_404
from django.urls.base import reverse
from django.shortcuts import redirect

class DeleteDirectMessageView(LoginRequiredMixin, generic.DeleteView):
    model: Model = DirectMessage

    def delete(self, request, *arts, **kwargs):
        sender_direct_message_pk = self.kwargs['pk']
        sender_direct_message = DirectMessage.objects.get(id=sender_direct_message_pk)
        addressee_direct_message = DirectMessage.objects.get(id=sender_direct_message.recipient_message.id)
        success_url = self.get_success_url()
        sender_direct_message.delete()
        addressee_direct_message.delete()
        return redirect(success_url)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self) -> str:
        direct_message_pk = self.kwargs['pk']
        direct_message = get_object_or_404(DirectMessage, pk=direct_message_pk)
        dm_room_pk = direct_message.room.id
        return reverse('chat:dm_room_detail', kwargs={'pk': dm_room_pk})