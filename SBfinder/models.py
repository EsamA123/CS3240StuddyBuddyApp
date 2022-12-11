from django.db import models
from django.conf import settings #Foreign Key?

# Create your models here.


class SubjData(models.Model):
    subject = models.CharField(max_length=4)        #Added to store all possible subjects in the database
    def __str__(self):
        return self.subject

class UserInfo(models.Model):
    user_name = models.CharField(max_length = 200)
    user_email = models.EmailField(max_length = 254)
    correspond_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.user_name


class Course(models.Model):
    instructor = models.CharField(max_length=100, blank = True, null = True)
    course_number = models.CharField(max_length=100, blank = True, null = True)
    subject = models.CharField(max_length=100, blank = True, null = True)
    catalog_number = models.CharField(max_length=100, blank = True, null = True)
    description = models.CharField(max_length=100, blank = True, null = True)
    course_section = models.CharField(max_length=100, blank = True, null = True)
    meetings = models.CharField(max_length=100, blank = True, null = True)
    component = models.CharField(max_length=100, blank = True, null = True)
    users = models.ManyToManyField(UserInfo)

    def __str__(self):
        return self.course_number

