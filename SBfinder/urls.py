from django.urls import path

from . import views

app_name = 'SBfinder'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('classes/', views.getClasses, name='class'),
    path('createuser/', views.create_user, name = 'create_user'),
    path('<slug:slug>/userprofile/', views.UserProfileView.as_view(), name = 'profile'),
]