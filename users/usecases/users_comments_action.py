from communities.models import Communities
from news_posts.models import Comment

def users_comments_action(context: dict, pk: int) -> dict:
    context['comments_list'] = Comment.objects.filter(user=pk).order_by("-created_at")
    context['communities_list'] = Communities.objects.filter(member=pk).order_by("-created_at")
    return context

    