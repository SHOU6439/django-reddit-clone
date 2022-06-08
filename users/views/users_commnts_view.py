from django.contrib.auth.mixins import LoginRequiredMixin
from news_posts.models import Comment
from django.contrib.auth import get_user_model
from django.views import generic
from communities.models import Communities

class UsersCommentsView(LoginRequiredMixin, generic.DetailView):
    User = get_user_model()
    model = User
    template_name = 'users/comments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_list'] = Comment.objects.filter(user=self.kwargs['pk']).order_by("-created_at")
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        return context
