from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from news_posts.models import NewsPosts, Notification, Like
from django.contrib.auth.decorators import login_required
from django.db import transaction


@login_required
@transaction.atomic
def like(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    post = NewsPosts.objects.get(pk=pk)
    like = Like.objects.filter(liked_user=request.user, liked_post=post).first()
    notification = Notification
    message = request.user.username + "が      " + post.title + "      をいいねした。"
    like_notification = notification.objects.filter(title="いいね通知", message=message, destination=post.user)
    if like:
        # NOTE:いいねされた順に投稿を並べたいときに、いいねを一度解除し、再度いいねした場合、そのいいねされた順をリセットしたいためこのような実装になった
        Like.objects.filter(liked_user=request.user, liked_post=post).delete()
    if not like:
        # likeオブジェクトが存在しないときにlikeオブジェクトを作成する
        like = Like()
        like.liked_user = request.user
        like.liked_post = post
        like.is_liked = False
    if like.is_liked == False:
        # いいねをする
        like.is_liked = True
        post.like += 1
        if not like_notification and like.liked_post.user != request.user:
            notification.objects.create(title="いいね通知", message=message, destination=post.user)
    else:
        # いいねを解除する
        like.is_liked = False
        post.like -= 1
    like.save()
    post.save()
    return redirect('users:liked_posts', pk=request.user.id)
