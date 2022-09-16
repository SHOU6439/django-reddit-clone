from django.utils import timezone
from django.forms import ModelForm
from django.http import HttpRequest
from chat.models.dm_room import DMRoom
from chat.models.direct_message import DirectMessage
from django.contrib.auth import get_user_model


def post_direct_message_action(request: HttpRequest, form: ModelForm, author_room: DMRoom, addressee_room: DMRoom, addressee_pk: int):
    User = get_user_model()
    author = User.objects.get(id=request.user.id)
    addressee = User.objects.get(id=addressee_pk)
    post_data = form.save(commit=False)
    post_data.sender = get_user_model().objects.get(id=request.user.id)
    post_data.room = author_room
    post_data.save()
    if addressee_room:
        get_addressee_room = DMRoom.objects.get(author=addressee, addressee=author)
        DirectMessage.objects.create(room=get_addressee_room, sender=author, content=post_data.content)
        sender_message = DirectMessage.objects.get(id=post_data.id)
        recipient_message = DirectMessage.objects.get(room=get_addressee_room, sender=author, content=post_data.content)
        sender_message.recipient_message = recipient_message
        sender_message.save()
