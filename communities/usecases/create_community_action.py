from communities.forms import CommunityForm
from users.models.user import User
from django.contrib.auth import get_user_model
from communities.models import Communities

def create_community_action(user: User, post_data: Communities) -> Communities:
    post_data.admin = get_user_model().objects.get(id=user.id)
    post_data.save()
    community = Communities.objects.get(name=post_data.name)
    # adminがコミュニティを作ったら自動的にadminはmemberに追加する
    community.member.add(user.id)
    community.save()
    return community
