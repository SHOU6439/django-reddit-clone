from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from communities.forms import CommunityForm
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