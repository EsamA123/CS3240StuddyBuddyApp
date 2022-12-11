from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import SubjData, Course
from django.contrib import admin
from .models import UserInfo

import requests

class IndexView(generic.ListView):
    template_name = 'SBfinder/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return 0;

def getClasses(request):
    #model = Course
    data = None
    classes=[]
    if 'subjSearch' in request.GET:     #Check if the inputed search is a valid class subject
        subj = request.GET['subjSearch']
        url = "http://luthers-list.herokuapp.com/api/dept/" + subj +"?format=json"  #If subj is valid create the api link
        response = requests.get(url)                                                #for the cooresponding department
        data = response.json()
    if 'numSearch' in request.GET:     #Check if the inputed search is a valid class number
        catNumb = request.GET['numSearch']
        for i in data:
            num = i['catalog_number']
            if num == catNumb:
                classes.append(i)
    return render(request, 'SBfinder/class.html', { "test": classes})   #Update their website with the subjects classes, changed url to class from /index

def create_user(request):
    obj, created = UserInfo.objects.get_or_create(
        user_name = request.user.username,
        user_email = request.user.email,
        correspond_user = request.user,
        slug = request.user.username

    )

    return HttpResponseRedirect(reverse('SBfinder:class'))

def add_to_schedule(request):
    obj, created = Course.objects.get_or_create(
        course_number = request.POST['class_num'],
    )

    current_userInfo = UserInfo.objects.get(correspond_user = request.user)

    obj.users.add(current_userInfo)

    return HttpResponseRedirect(reverse('SBfinder:profile', args=(current_userInfo.slug,)))
class UserProfileView(generic.DetailView):
    model = UserInfo
    template_name = 'SBfinder/userProfile.html'
    context_object_name = "userInfo"



