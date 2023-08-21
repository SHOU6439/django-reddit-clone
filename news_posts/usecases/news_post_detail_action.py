from users.models import User
from news_posts.models import NewsPosts
from news_posts.models import NewsPosts, Comment, Like

def news_post_detail_action(user: User, post: NewsPosts, context: dict):
    like_status = Like.objects.filter(liked_post=post.id, liked_user=user)
    context['comment_list'] = Comment.objects.filter(target=post.id).order_by("-latest_replayed_at", "-created_at")
    context['member_count'] = User.objects.filter(member=post.community).count()
    context['community_post_count'] = NewsPosts.objects.filter(community_id=post.community).count()
    context['saved_posts'] = NewsPosts.objects.filter(saved_user=user.id)
    if like_status:
        context['like_status'] = Like.objects.get(liked_post=post.id, liked_user=user)