from django import forms
from django.forms import fields
from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=128)
    email = forms.EmailField()
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    password1 = forms.CharField(required=False)
    password2 = password1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field, value in zip(self.fields, self.fields.values()):
            value.widget.attrs["class"] = 'input-userinfo-textarea'
            value.widget.attrs["placeholder"] = field.upper()
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class LoginForm(AuthenticationForm):
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field, value in zip(self.fields, self.fields.values()):
            value.widget.attrs["class"] = 'input-userinfo-textarea'
            value.widget.attrs["placeholder"] = field.upper()
    class Meta:
        model = User
        fields = ('email', 'password')