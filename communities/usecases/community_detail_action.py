from users.models.user import User
from communities.models import Communities
from news_posts.models import NewsPosts

def community_detail_action(user: User, pk: int, context: dict):
    context['member_count'] = User.objects.filter(member=pk).count()
    context['is_joined'] = Communities.objects.filter(member=user)
    context['current_community'] = Communities.objects.get(id=pk)
    context['saved_posts'] = NewsPosts.objects.filter(saved_user=user.id)