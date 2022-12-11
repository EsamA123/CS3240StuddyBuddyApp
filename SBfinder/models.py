from django.db import models
from django.conf import settings #Foreign Key?
from django.utils.timezone import now

# Create your models here.


class SubjData(models.Model):
    subject = models.CharField(max_length=4)        #Added to store all possible subjects in the database
    def __str__(self):
        return self.subject

class UserInfo(models.Model):
    user_name = models.CharField(max_length = 255)
    user_email = models.EmailField(max_length = 255)
    correspond_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    slug = models.SlugField(null=True, max_length = 255)
    friends = models.ManyToManyField("self", blank = True)

    def __str__(self):
        return self.user_name

class Friend_Request(models.Model):
    from_user = models.ForeignKey(UserInfo, related_name = 'from_user', on_delete= models.CASCADE)
    to_user = models.ForeignKey(UserInfo, related_name='to_user', on_delete=models.CASCADE)

    def __str__(self):
        return "From" + self.from_user.user_name + " to " + self.to_user.user_name

class ForumPage(models.Model):
    course_id = models.CharField(max_length=255, blank = True, null = True)
    def __str__(self):
        return str(self.course_id)

class Course(models.Model):
    instructor = models.CharField(max_length=255, blank = True, null = True)
    course_number = models.CharField(max_length=255, blank = True, null = True)
    subject = models.CharField(max_length=255, blank = True, null = True)
    catalog_number = models.CharField(max_length=255, blank = True, null = True)
    description = models.CharField(max_length=255, blank = True, null = True)
    course_section = models.CharField(max_length=255, blank = True, null = True)
    meetings = models.CharField(max_length=255, blank = True, null = True)
    component = models.CharField(max_length=255, blank = True, null = True)
    users = models.ManyToManyField(UserInfo)
    #forum_page = ForumPage.objects.create(forum_page_id=self_id)
    forum_page = models.ManyToManyField(ForumPage)
    #forum_page = models.ForeignKey(ForumPage, blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        representation_list = str(list(self.users.all())) + "|" + str(self.subject) + " " + str(self.catalog_number) + " " +str(self.description) + "|" + str([user.pk for user in self.users.all()])

        return representation_list

class Forum(models.Model):
    #name = models.CharField(max_length=200, default="anonymous")
    #email = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    #forum_page = models.ForeignKey(ForumPage, blank=True, on_delete=models.CASCADE)
    forum_page = models.ManyToManyField(ForumPage)
    #link = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.topic)

class Discussion(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forum)
