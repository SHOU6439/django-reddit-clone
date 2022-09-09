from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from chat.models import DirectMessage, DMRoom
from django.db.models import Model
from django.shortcuts import get_object_or_404
from django.urls.base import reverse

class DeleteDirectMessageView(LoginRequiredMixin, generic.DeleteView):
    model: Model = DirectMessage
    def get_success_url(self) -> str:
        direct_message_pk = self.kwargs['pk']
        direct_message = get_object_or_404(DMRoom, pk=direct_message_pk)
        dm_room_pk = direct_message.room.id
        return reverse('news_posts:dm_room_detail', kwargs={'pk': dm_room_pk})