from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from users.forms import ProfileEditForm
from users.models import User
from django.urls import reverse


class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = ProfileEditForm
    template_name = 'users/profile_edit.html'
    def get_success_url(self):
        return reverse('users:detail', kwargs={'pk': self.request.user.id})

    def get_object(self):
        return self.request.user
