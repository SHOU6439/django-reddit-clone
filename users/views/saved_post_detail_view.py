from django.contrib.auth.mixins import LoginRequiredMixin
from news_posts.models import NewsPosts
from django.contrib.auth import get_user_model
from django.views import generic
from communities.models import Communities


class SavedPostDetailView(LoginRequiredMixin, generic.DetailView):
    User = get_user_model()
    model = User
    template_name = 'users/saved_post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        context['saved_posts'] = NewsPosts.objects.filter(saved_user=self.kwargs['pk']).order_by("saved_at__created_at").reverse()
        return context