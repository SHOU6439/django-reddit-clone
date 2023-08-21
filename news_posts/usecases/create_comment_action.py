from news_posts.forms import CreateCommentForm
from django.shortcuts import get_object_or_404
from news_posts.models import NewsPosts, Notification
from users.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone

def create_comment_action(user: User, form: CreateCommentForm, post_pk: int):
    post = get_object_or_404(NewsPosts, pk=post_pk)
    comment = form.save(commit=False)
    notification = Notification
    title = user.username + "が      " + post.title + "      に対してコメントした"
    # comment_notification = notification.objects.filter(title=title, message=comment.content, destination=post.user)
    comment.target = post
    comment.user = get_user_model().objects.get(id=user.id)
    comment.save()
    # comment_query = Comment.objects.filter(
    #     target=post,
    #     user=get_user_model().objects.get(id=self.request.user.id),
    #     content=comment.content
    # )
    notification.objects.create(title=title, message=comment.content, destination=post.user)
    post.latest_commented_at = timezone.now()
    post.save()

    # if not comment_query:
    #     comment_notification.delete()
    