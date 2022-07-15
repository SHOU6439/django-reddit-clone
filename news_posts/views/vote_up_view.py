#こちらのファイルは現在使われておりません。
from django.shortcuts import redirect
from news_posts.models import NewsPosts, Notification, Vote
from django.contrib.auth.decorators import login_required
from django.db import transaction


@login_required
@transaction.atomic
def vote_up(request, pk):
    post = NewsPosts.objects.get(pk=pk)
    vote = Vote.objects.filter(voted_user=request.user, voted_post=post).first()
    notification = Notification
    message = request.user.username + "が      " + post.title + "      を賛成した。"
    vote_notification = notification.objects.filter(title="vote通知", message=message, destination=post.user)
    if vote:
        # もうすでに何度かvoteをしてるとき
        Vote.objects.filter(voted_user=request.user, voted_post=post).delete()
    if not vote:
        # まだvoteをしたことがない、もしくは一度voteを取り消したとき
        vote = Vote()
        vote.voted_user = request.user
        vote.voted_post = post
        vote.flag = 0
    if vote.flag <= 0:
        # downをしてる、もしくは何もvoteしてないとき
        vote.flag += 1
        post.vote += 1
        if not vote_notification and vote.voted_post.user.id == request.user:
            notification.objects.create(title="vote通知", message=message, destination=post.user)
    else:
        # voteしたことを取り消すとき
        vote.flag -= 1
        post.vote -= 1
    vote.save()
    post.save()
    return redirect('users:up_voted_posts', pk=request.user.id)
