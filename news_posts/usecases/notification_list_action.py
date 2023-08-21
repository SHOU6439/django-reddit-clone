from users.models.user import User
from news_posts.models.notification import Notification

def notification_list_action(user: User, context: dict):
    context['notification_list'] = Notification.objects.filter(destination=user).order_by("-created_at")
        