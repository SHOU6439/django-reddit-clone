from chat.models import DirectMessage


def delete_direct_message_action(sender_direct_message_pk):
    try:
        sender_direct_message = DirectMessage.objects.get(id=sender_direct_message_pk)
        addressee_direct_message = DirectMessage.objects.get(id=sender_direct_message.recipient_message.id)
        sender_direct_message.delete()
        addressee_direct_message.delete()
    except Exception:
        sender_direct_message = DirectMessage.objects.get(id=sender_direct_message_pk)
        sender_direct_message.delete()
