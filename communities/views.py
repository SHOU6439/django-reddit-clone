from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from communities.forms import CommunityForm
from news_posts.models import NewsPosts
from .models import Communities
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
# Create your views here.
class CreateCommunityView(LoginRequiredMixin, generic.CreateView):
    template_name = 'communities/create_community.html'
    model = Communities
    form_class = CommunityForm
    success_url = reverse_lazy('news_posts:index')
    def post(self, request):
        form = CommunityForm(request.POST)

        get_user_id = form.save(commit=False)
        get_user_id.admin = get_user_model().objects.get(id=request.user.id)
        get_user_id.save()
        return redirect('news_posts:index')

class CommunityDetailView(LoginRequiredMixin, generic.DetailView):
    model = Communities
    template_name = 'communities/community_detail.html'

    def get_context_data(self, **kwargs,):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['communitypost_list'] = NewsPosts.objects.filter(community_id=pk).order_by("-created_at")
        return context