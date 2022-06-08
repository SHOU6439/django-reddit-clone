from django.shortcuts import redirect
from news_posts.models import Notification
from communities.models import Communities
from django.contrib.auth.decorators import login_required

@login_required
def join(request, pk):
    community = Communities.objects.get(pk=pk)
    notification = Notification
    message = request.user.username + "が      " + community.name + "      に加入した!"
    join_notification = notification.objects.filter(title="communityメンバー加入通知", message=message, destination=community.admin)
    community.member.add(request.user.id)
    community.save()
    # 直近にcommunityをleaveした場合にjoin_notificationを作り直す
    if join_notification:
        join_notification.delete()
    if not join_notification:
        notification.objects.create(title="communityメンバー加入通知", message=message, destination=community.admin)
    return redirect('communities:detail', pk=pk)
