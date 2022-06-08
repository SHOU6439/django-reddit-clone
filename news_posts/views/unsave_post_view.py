from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic
from users.models import User
from news_posts.models import NewsPosts

class UnSavePostView(LoginRequiredMixin, generic.View):
    model = NewsPosts

    def get(self, request, *args, **kwargs):
        post = NewsPosts.objects.get(pk=self.kwargs['pk'])
        user = User.objects.get(id=request.user.id)
        user.saved_post.remove(post)
        return redirect('users:saved_posts', pk=self.request.user.id)