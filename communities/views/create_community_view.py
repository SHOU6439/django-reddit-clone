from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.views import generic
from communities.forms import CommunityForm
from communities.models import Communities
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.db.models import Model
from django.forms import ModelForm
from communities.usecases.create_community_action import create_community_action

class CreateCommunityView(LoginRequiredMixin, generic.CreateView):
    template_name: str = 'communities/create_community.html'
    model: Model = Communities
    form_class: ModelForm = CommunityForm
    success_url = reverse_lazy('news_posts:hot_index')

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        form = CommunityForm(request.POST)
        
        if form.is_valid():
            post_data = form.save(commit=False)
            community = create_community_action(request.user, post_data)
            return redirect('communities:detail', pk=community.id)
        return redirect('communities:create')