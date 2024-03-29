from django import forms
from django.forms import fields, widgets
from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    password1 = forms.CharField(required=False)
    password2 = password1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = ('ユーザー名', 'メールアドレス', 'パスワード')
        for placeholder, value in zip(placeholders, self.fields.values()):
            value.widget.attrs["class"] = 'input-userinfo-textarea'
            value.widget.attrs["placeholder"] = placeholder
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = ('ユーザー名', 'パスワード')
        for placeholder, value in zip(placeholders, self.fields.values()):
            value.widget.attrs["class"] = 'input-userinfo-textarea'
            value.widget.attrs["placeholder"] = placeholder
    class Meta:
        model = User
        fields = ('username', 'password')

class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(max_length=20, widget=forms.widgets.TextInput(attrs={'class': "profile-edit-new-name-input-textarea", 'placeholder': "表示名"}))
    about = forms.CharField(max_length=200, widget=forms.widgets.Textarea(attrs={'class': "profile-edit-new-user-about-input-textarea", 'placeholder': "自己紹介"}), required=False)

    class Meta:
        model = User
        fields = ('username', 'about', 'photo', 'header_photo')
