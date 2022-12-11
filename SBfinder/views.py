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
from .models import UserInfo, Friend_Request
import json
import requests
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(generic.ListView):
    template_name = 'SBfinder/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return 0;


def getClasses(request):
    # model = Course // I don't think this is needed here
    data = None
    classes = []
    if 'subjSearch' in request.GET:  # Check if the inputed search is a valid class subject
        subj = request.GET['subjSearch'].upper()
        url = "http://luthers-list.herokuapp.com/api/dept/" + subj + "?format=json"  # If subj is valid create the api link
        response = requests.get(url)  # for the cooresponding department
        data = response.json()

    if 'numSearch' in request.GET:  # Check if the inputed search is a valid class number
        catNumb = request.GET['numSearch']
        if catNumb != "":
            for i in data:
                num = i['catalog_number']
                if num == catNumb:
                    classes.append(i)
        else:
            for i in data:
                classes.append(i)

    return render(request, 'SBfinder/class.html',
                  {"test": classes})  # Update their website with the subjects classes, changed url to class from /index


def create_user(request):
    obj, created = UserInfo.objects.get_or_create(
        user_name=request.user.username,
        user_email=request.user.email,
        correspond_user=request.user,
        slug=request.user.username
    )

    return HttpResponseRedirect(reverse('SBfinder:class'))


def add_to_schedule(request):
    # load the context variable via POST; replace single quotation with double quotation
    class_added = json.loads(request.POST['class'].replace("\'", "\""))

    obj, created = Course.objects.get_or_create(
        instructor=class_added['instructor'],
        subject=class_added['subject'],
        course_number=class_added['course_number'],
        catalog_number=class_added['catalog_number'],
        description=class_added['description'],
        course_section=class_added['course_section'],
        meetings=class_added['meetings'],
        component=class_added['component'],

    )

    current_userInfo = UserInfo.objects.get(correspond_user=request.user)

    obj.users.add(current_userInfo)

    return HttpResponseRedirect(reverse('SBfinder:profile', args=(current_userInfo.slug,)))


def delete_from_schedule(request, id):
    c = Course.objects.get(id=id)
    current_userInfo = UserInfo.objects.get(correspond_user=request.user)
    c.users.remove(current_userInfo)
    return HttpResponseRedirect(reverse('SBfinder:profile', args=(current_userInfo.slug,)))


def generate_SB(request):

    result_nameDic = {}

    SB_class_list = request.POST.getlist('checks')

    # Get the current user to make sure we are not adding the current user to our SB list
    current_userInfo = UserInfo.objects.get(correspond_user=request.user)

    for SB in SB_class_list:
        Splitted = SB.split("|")
        idList = Splitted[2]
        idList = idList.replace("[", "")
        idList = idList.replace("]", "")
        idList = idList.split(",")
        for i in range(len(Splitted[0].split(","))):
            name = Splitted[0].split(",")[i]
            name = name.replace("[", "")
            name = name.replace("]", "")
            name = name.replace("<UserInfo: ", "")
            name = name.replace(">", "")

            if str(name) + idList[i] not in result_nameDic.keys():
                if str(name) != current_userInfo.user_name and int(idList[i]) != current_userInfo.pk:
                    result_nameDic[str(name) + idList[i]] = []

            if str(name) != current_userInfo.user_name and int(idList[i]) != current_userInfo.pk:
                result_nameDic[str(name) + idList[i]].append(Splitted[1])

    return render(request, 'SBfinder/SB_list.html', {"SB_Dic": result_nameDic})


# Send Friend Request
@login_required
def send_friend_request(request, userID):
    userID = int(userID)
    from_user = UserInfo.objects.get(correspond_user=request.user)
    to_user = UserInfo.objects.get(pk=userID)
    friend_request, created = Friend_Request.objects.get_or_create(from_user=from_user, to_user=to_user)

    # Ideally redirect users to a fancier page
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request was already sent')


# Accept Friend Request
@login_required
def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(pk=requestID)
    if friend_request.to_user == UserInfo.objects.get(correspond_user=request.user):
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')

    else:
        return HttpResponse('friend request not accepeted')


@method_decorator(login_required, name='dispatch')
class UserProfileView(generic.DetailView):
    model = UserInfo

    # the currently logged-in user cannot switch to other user profiles by changing the url because we are obly getting the
    # userInfo objects that correspond to the currently logged in user
    def get_object(self, queryset=None):
        return get_object_or_404(UserInfo, correspond_user=self.request.user)

    template_name = 'SBfinder/userProfile.html'
    context_object_name = "userInfo"


class friendView(generic.ListView):
    template_name = 'SBfinder/friend_request.html'
    model = Friend_Request
    context_object_name = "friend_request"

