from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import admin

from .models import UserInfo


class IndexView(generic.ListView):
    template_name = 'SBfinder/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return 0;

def create_user(request):
    obj, created = UserInfo.objects.get_or_create(
        user_name = request.user.username,
        user_email = request.user.email,
        correspond_user = request.user,
        slug = request.user.username

    )

    return HttpResponseRedirect(reverse('SBfinder:profile', args = (obj.slug,)))

class UserProfileView(generic.DetailView):
    model = UserInfo
    template_name = 'SBfinder/userProfile.html'
    context_object_name = "userInfo"


