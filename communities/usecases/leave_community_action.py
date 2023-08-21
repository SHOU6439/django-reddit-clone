from users.models import User
from news_posts.models import Notification
from communities.models import Communities

def leave_community_action(user: User, pk: int):
    community = Communities.objects.get(pk=pk)
    notification = Notification
    message = user.username + "が      " + community.name + "      を離脱した..."
    leave_notification = notification.objects.filter(title="communityメンバー離脱通知", message=message, destination=community.admin)
    community.member.remove(user.id)
    community.save()
    # 直近にcommunityをjoinした場合にleave_notificationを作り直す
    if leave_notification:
        leave_notification.delete()
    if not leave_notification:
        notification.objects.create(title="communityメンバー離脱通知", message=message, destination=community.admin)
    