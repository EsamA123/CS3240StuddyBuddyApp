from django.forms import ModelForm
from .models import *


class CreateInForum(ModelForm):
    class Meta:
        model = Forum
        fields = ['topic', 'description']


class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = ['discuss']