from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from users.models import User
from news_posts.models import NewsPosts
from django.db.models import Model
from news_posts.usecases.unsave_post_action import unsave_post_action

class UnSavePostView(LoginRequiredMixin, generic.View):
    model: Model = NewsPosts

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponseRedirect:
        post = NewsPosts.objects.get(pk=self.kwargs['pk'])
        user = User.objects.get(id=request.user.id)
        unsave_post_action(user, post)
        return redirect('users:saved_posts', pk=self.request.user.id)