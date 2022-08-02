from chat.models import DMRoom, DMInvite


def create_dm_room_acton(author, addressee, author_room, addressee_room):
    if not author_room:
        # author側でDMルームを作成
        DMRoom.objects.create(author=author, addressee=addressee)

    dm_invite = DMInvite.objects.filter(invited_user=author, received_user=addressee)
    dm_receive = DMInvite.objects.filter(invited_user=addressee, received_user=author)
    if not dm_invite:
        # DM招待を作成
        get_author_room = DMRoom.objects.filter(author=author, addressee=addressee).first()
        DMInvite.objects.create(room=get_author_room, invited_user=author, received_user=addressee)
        if author_room and addressee_room:
            # DMルームが既に双方に存在する場合既にDM招待は承認されてるので削除。
            dm_invite.delete()
    if dm_receive:
        # 受信する側からもDM招待を送られた場合は双方のDM招待を削除し、そのまま双方にDMルームを作成。実質DM招待の承認と同じ動きをします。
        dm_invite.delete()
        dm_receive.delete()
