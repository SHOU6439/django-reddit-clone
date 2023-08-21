from django.http import HttpRequest
from users.forms import UserForm
from django.contrib.auth import authenticate, login, get_user_model

def signup_action(request: HttpRequest, form: UserForm):
    User = get_user_model()
    username = form.cleaned_data.get('username')
    email = form.cleaned_data.get('email')
    password = form.cleaned_data.get('password')

    user = User.objects.create_user(username, email, password)
    user.save()
    auth_user = authenticate(request, username=username, password=password)
    login(request, auth_user)