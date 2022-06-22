from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from users.models import User
from news_posts.models import NewsPosts, Comment, Like

class NewsPostDetailView(LoginRequiredMixin, generic.DetailView):
    model = NewsPosts
    template_name = 'news_posts/post_detail.html'
    def get_context_data(self, **kwargs):
        post_pk = self.kwargs['pk']
        post = NewsPosts.objects.get(id=post_pk)
        like_status = Like.objects.filter(liked_post=post_pk, liked_user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(target=post_pk).order_by("-latest_replayed_at", "-created_at")
        context['member_count'] = User.objects.filter(member=post.community).count()
        context['community_post_count'] = NewsPosts.objects.filter(community_id=post.community).count()
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.request.user.id)
        if like_status:
            context['like_status'] = Like.objects.get(liked_post=post_pk, liked_user=self.request.user)
        return context