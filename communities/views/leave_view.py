from django.shortcuts import redirect
from news_posts.models import Notification
from communities.models import Communities
from django.contrib.auth.decorators import login_required



@login_required
def leave(request, pk):
    community = Communities.objects.get(pk=pk)
    notification = Notification
    message = request.user.username + "が      " + community.name + "      を離脱した..."
    leave_notification = notification.objects.filter(title="communityメンバー離脱通知", message=message, destination=community.admin)
    community.member.remove(request.user.id)
    community.save()
    # 直近にcommunityをjoinした場合にleave_notificationを作り直す
    if leave_notification:
        leave_notification.delete()
    if not leave_notification:
        notification.objects.create(title="communityメンバー離脱通知", message=message, destination=community.admin)
    return redirect('communities:detail', pk=pk)