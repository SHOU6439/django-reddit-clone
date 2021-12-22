from django import forms
from django.db.models import fields
from .models import Comment, NewsPosts
from communities.models import Communities


class CreatePostForm(forms.ModelForm):
    CHOICES = Communities.objects.all()
    title = forms.CharField(max_length=300, widget=forms.widgets.TextInput(attrs={'class': "post-title-input-textarea", 'placeholder': "Title"}))
    content = forms.CharField(max_length=512, widget=forms.widgets.Textarea(attrs={'class': "post-content-input-textarea", 'placeholder': "Text(Optional)"}))
    # community = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class': "post-select-community-field"}, choices=CHOICES))

    class Meta:
        model = NewsPosts
        fields = ('title', 'content' , 'photo', 'community')

class CreateCommentForm(forms.ModelForm):
    content = forms.CharField(max_length=512, widget=forms.widgets.Textarea(attrs={'class':"comment-content-input-textarea", 'placeholder': "What are your thoughts?"}))

    class Meta:
        model = Comment
        fields = ('content',)

class NewsPostEditForm(forms.ModelForm):
    content = forms.CharField(max_length=512, widget=forms.widgets.Textarea(attrs={'class': "post-content-input-textarea-edit", 'placeholder': "Text(Optional)"}))
    class Meta:
        model = NewsPosts
        fields = ('content',)