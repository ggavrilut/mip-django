from django.forms import ModelForm
from .models import Entry, Tag


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'teaser', 'body')


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)