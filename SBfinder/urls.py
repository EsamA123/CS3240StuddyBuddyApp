from django.urls import path

from . import views

app_name = 'SBfinder'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('classes/', views.getClasses, name='class'),
    path('createuser/', views.create_user, name = 'create_user'),
    path('<slug:slug>/userprofile/', views.UserProfileView.as_view(), name = 'profile'),
    path('addtoschedule/', views.add_to_schedule, name='add_to_schedule'),
    path('deletefromschedule/<int:id>', views.delete_from_schedule, name='delete_from_schedule'),
    path('studyBuddyList/', views.generate_SB, name = 'generate_SB'),
    path('send_friend_request/<str:userID>/', views.send_friend_request, name = "SFR"),
    path('accept_friend_request/<int:requestID>/', views.accept_friend_request, name = "AFR"),
    path('friendrequest/', views.friendView.as_view(), name = 'friend_request'),
    path('accept_SS_request/<int:requestID>/', views.accept_SS_request, name='ASR'),
    path('studysession/', views.studyView.as_view(), name = 'study_session'),
    path('generateSS/', views.generateSSView.as_view(), name = 'generate_SS'),
    path('createSS/', views.create_SS, name = 'create_SS'),
    path('leaveSS/<int:id>', views.leave_study_session, name='leave_study_session'),
    path('message/<int:id>', views.message_log, name = 'message_log'),
    path('generate_message/<int:id>', views.generate_message, name = 'generate_message'),


]