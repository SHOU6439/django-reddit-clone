from django import forms
from django.db.models import fields
from django.db.models.fields import BLANK_CHOICE_DASH
from communities.models import Communities
from django.utils.safestring import mark_safe


class CommunityForm(forms.ModelForm):
    help_format = (
        '<i class="{}" style="height:16px; width:16px;"></i>'
        '<span class="community-type-radio-item-name">{}</span>'
        '<span class="community-type-description">{}</span>'
    )
    name = forms.CharField(max_length=21, widget=forms.widgets.TextInput(attrs={'class': "community-name-input-textarea"}))
    community_type = forms.fields.ChoiceField(
        choices = (
            ('0', mark_safe(help_format.format('fas fa-user', '公開', '誰でもこのコミュニティを閲覧、投稿、コメントすることができます。'))),
            ('1', mark_safe(help_format.format('far fa-eye', '制限あり', 'このコミュニティは誰でも閲覧できますが、投稿できるのは承認されたユーザーだけです。'))),
            ('2', mark_safe(help_format.format('fas fa-lock', '非公開', '承認されたユーザーだけがこのコミュニティを閲覧し、投稿することができます。'))),
        ),
        required=True,
        widget=forms.widgets.RadioSelect(attrs={'class': "community-type-select-radio-button"}),
    )
    is_nsfw = forms.BooleanField(
        widget=forms.widgets.CheckboxInput(attrs={'class':"community-is-nsfw-check"}),
        required=False
    )

    class Meta:
        model = Communities
        fields = ('name', 'community_type', 'is_nsfw')