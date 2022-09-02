from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.views import generic
from users.forms import ProfileEditForm
from users.models import User
from django.urls import reverse
from django.db.models import Model

class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    model: Model = User
    form_class: ModelForm = ProfileEditForm
    template_name: str = 'users/profile_edit.html'
    def get_success_url(self) -> str:
        return reverse('users:detail', kwargs={'pk': self.request.user.id})

    def get_object(self) -> User:
        return self.request.user
