from django.forms import ModelForm
from users.forms import LoginForm
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginView(views.LoginView):
    form_class: UserCreationForm = LoginForm
    template_name: str = 'users/login.html'