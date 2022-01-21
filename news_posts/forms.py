from django import forms
from .models import Comment, NewsPosts
from communities.models import Communities
from users.models import User


class CreatePostForm(forms.ModelForm):
    # CHOICES = Communities.objects.filter(member=current_user)
    title = forms.CharField(max_length=300, widget=forms.widgets.TextInput(attrs={'class': "post-title-input-textarea", 'placeholder': "Title"}))
    content = forms.CharField(max_length=512, widget=forms.widgets.Textarea(attrs={'class': "post-content-input-textarea", 'placeholder': "Text(Optional)"}))
    # community = forms.ModelChoiceField(queryset=Communities.objects.filter(member=1))
    # def __init__(self, user, *args, **kwargs):
    #     super(CreatePostForm, self).__init__(*args, **kwargs)
    #     self.fields['community'].queryset = User.objects.filter(id=user.id)

    class Meta:
        model = NewsPosts
        fields = ('title', 'content', 'photo', 'community')

class CreateCommentForm(forms.ModelForm):
    content = forms.CharField(max_length=512, widget=forms.widgets.Textarea(attrs={'class':"comment-content-input-textarea", 'placeholder': "What are your thoughts?"}))

    class Meta:
        model = Comment
        fields = ('content',)

# class CreateReplayForm(forms.ModelForm):
#     mension = forms.CharField(max_length=20, widget=forms.widgets.TextInput(attrs={'class':"replay-mension-input-textarea", 'placeholder': "Who do you want to reply to?"}))
#     content = forms.CharField(max_length=512, widget=forms.widgets.Textarea(attrs={'class':"replay-content-input-textarea", 'placeholder': "What are your thoughts?"}))

#     class Meta:
#         model = Replay
#         fields = ('mension', 'content')

class NewsPostEditForm(forms.ModelForm):
    content = forms.CharField(max_length=512, widget=forms.widgets.Textarea(attrs={'class': "post-content-input-textarea-edit", 'placeholder': "Text(Optional)"}))
    class Meta:
        model = NewsPosts
        fields = ('content',)