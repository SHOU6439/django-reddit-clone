from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from news_posts.models import NewsPosts, Like
from django.contrib.auth.decorators import login_required
from django.db import transaction
from news_posts.usecases.like_action import like_action


@login_required
@transaction.atomic
def like(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    post = NewsPosts.objects.get(pk=pk)
    like = Like.objects.filter(liked_user=request.user, liked_post=post).first()
    like_action(request.user, post, like)
    return redirect('users:liked_posts', pk=request.user.id)
