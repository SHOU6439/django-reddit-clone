from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from users.models import User, bookmarked_posts
from news_posts.models import NewsPosts
from django.db.models import Model

class SavePostView(LoginRequiredMixin, generic.View):
    model: Model = NewsPosts

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponseRedirect:
        post = NewsPosts.objects.get(pk=self.kwargs['pk'])
        user = User.objects.get(id=request.user.id)
        user.saved_post.add(post)
        count_save = bookmarked_posts.objects.filter(post=post).count()
        post.save_counter = count_save
        post.save()
        return redirect('users:saved_posts', pk=self.request.user.id)

