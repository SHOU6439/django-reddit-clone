from users.models.user import User
from news_posts.models.news_posts import NewsPosts
from news_posts.models.like import Like

def get_news_post_edit_form_action(user: User, post: NewsPosts, context: dict):
    like_status = Like.objects.filter(liked_post=post.id, liked_user=user)
    context['member_count'] = User.objects.filter(member=post.community).count()
    context['community_post_count'] = NewsPosts.objects.filter(community_id=post.community).count()
    context['saved_posts'] = NewsPosts.objects.filter(saved_user=user.id)
    if like_status:
        context['like_status'] = Like.objects.get(liked_post=post.id, liked_user=user)

    