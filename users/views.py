from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from news_posts.models import NewsPosts
from users.forms import LoginForm, ProfileEditForm, UserForm
from django.contrib.auth import views
from django.contrib.auth import authenticate, login, get_user_model
from django.views import generic
from communities.views import Communities
# Create your views here.

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.create_user(username, email, password)
            user.save()
            auth_user = authenticate(request, username=username, password=password)
            login(request, auth_user)
            return HttpResponseRedirect(reverse('news_posts:index'))
    else:
        form = UserForm()

        remove_forms = ['password1', 'password2']

    return render(request, 'users/signup.html', {'form': form, 'remove_forms': remove_forms})

class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


class ProfileDetailView(LoginRequiredMixin ,generic.DetailView):
    model = User
    template_name = 'users/profile_detail.html'
    # def get(self, request, *args, **kwargs):
    #     user_data = User.objects.get(id=request.user.id)

    #     return render(request, 'users/profile_detail.html', {
    #         'user_data': user_data,
    #     })
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userpost_list'] = NewsPosts.objects.filter(user_id=self.kwargs['pk']).order_by("-created_at")
        context['communities_list'] = Communities.objects.filter(member=self.kwargs['pk']).order_by("-created_at")
        return context

class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = 'users/profile_edit.html'
    def get_success_url(self):
        return reverse('users:detail', kwargs={'pk': self.request.user.id})

    def get_object(self):
        return self.request.user