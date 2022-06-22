from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views import generic
from users.models import User
from news_posts.models import NewsPosts, Like
from news_posts.forms import NewsPostEditForm


class NewsPostEditView(LoginRequiredMixin, generic.UpdateView):
    model = NewsPosts
    form_class = NewsPostEditForm
    template_name = 'news_posts/post_edit.html'
    def get_success_url(self):
        post_pk = self.kwargs['pk']
        return reverse('news_posts:post_detail', kwargs={'pk': post_pk})

    def get_context_data(self, **kwargs):
        post_pk = self.kwargs['pk']
        post = NewsPosts.objects.get(id=post_pk)
        like_status = Like.objects.filter(liked_post=post_pk, liked_user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['member_count'] = User.objects.filter(member=post.community).count()
        context['community_post_count'] = NewsPosts.objects.filter(community_id=post.community).count()
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.request.user.id)
        if like_status:
            context['like_status'] = Like.objects.get(liked_post=post_pk, liked_user=self.request.user)
        return context