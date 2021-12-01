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
            ('0', mark_safe(help_format.format('fas fa-user', 'Public', 'Anyone can view, post, and comment to this community'))),
            ('1', mark_safe(help_format.format('far fa-eye', 'Restricted', 'Anyone can view this community, but only approved users can post'))),
            ('2', mark_safe(help_format.format('fas fa-lock', 'Private', 'Only approved users can view and submit to this community'))),
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