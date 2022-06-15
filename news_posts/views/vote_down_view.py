from django.shortcuts import redirect
from news_posts.models import NewsPosts, Vote
from django.contrib.auth.decorators import login_required
from django.db import transaction

@login_required
@transaction.atomic
def vote_down(request, pk):
    post = NewsPosts.objects.get(pk=pk)
    vote = Vote.objects.filter(voted_user=request.user, voted_post=post).first()
    if vote:
        # もうすでに何度かvoteをしてるとき
        Vote.objects.filter(voted_user=request.user, voted_post=post).delete()
    if not vote:
        # まだvoteをしたことがない、もしくは一度voteを取り消したとき
        vote = Vote()
        vote.voted_user = request.user
        vote.voted_post = post
        vote.flag = 0
    if vote.flag >= 0:
        # upをしてる、もしくは何もvoteしてないとき
        vote.flag -= 1
        post.vote -= 1
    else:
        # voteしたことを取り消すとき
        vote.flag += 1
        post.vote += 1
    vote.save()
    post.save()
    return redirect('users:down_voted_posts', pk=request.user.id)
