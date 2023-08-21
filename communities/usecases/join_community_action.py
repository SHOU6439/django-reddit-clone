from news_posts.models import Notification
from communities.models import Communities
from users.models import User

def join_community_action(user: User, pk: int):
    community = Communities.objects.get(pk=pk)
    notification = Notification
    message = user.username + "が      " + community.name + "      に加入した!"
    join_notification = notification.objects.filter(title="communityメンバー加入通知", message=message, destination=community.admin)
    community.member.add(user.id)
    community.save()
    # 直近にcommunityをleaveした場合にjoin_notificationを作り直す
    if join_notification:
        join_notification.delete()
    if not join_notification:
        notification.objects.create(title="communityメンバー加入通知", message=message, destination=community.admin)
    