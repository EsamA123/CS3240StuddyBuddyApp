from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.urls import reverse
from SBfinder.models import Course

# Create your tests here.
class GoogleLoginTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.client = Client()
        self.user.save()

    def test_correct(self):
        #user = authenticate(username='test', password='12test12')
        #self.assertTrue((user is not None) and user.is_authenticated)
        self.client.login(username='test', password='12test12')

    '''def test_incorrect(self):
        #user = authenticate(username='test', password='12test12')
        #self.assertTrue((user is not None) and user.is_authenticated)
        self.client.login(username='test', password='wrongpass')
        self.assertFalse(user.is_authenticated)'''

    def test_successful_login(self):
        self.client.login(username='test', password='12test12')
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_correct_user_info(self):
        self.assertEquals(self.user.username, 'test')
        # don't include password because django doesn't store raw password but rather the hash of it
        self.assertEquals(self.user.email, 'test@example.com')

def create_course(instructor, course_number, subject, catalog_number, description, course_section,
                meetings, component, toggle, users):
    return Course.objects.create(instructor=instructor, course_number=course_number,
                                subject=subject, catalog_number=catalog_number, description=description,
                                course_section=course_section, meetings=meetings, component=component,
                                toggle=toggle, users=users)


class SearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.client = Client()
        self.user.save()
        self.client.login(username='test', password='12test12')
        user = auth.get_user(self.client)

    def test_no_courses(self):
        response = self.client.get(reverse('SBfinder:class'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No classes with the submitted subject")

    def correct_instructor(self):
        course = create_course(instructor = "Paul McBurney", course_number = "3240", subject = "CS", catalog_number = "123",
        description = "testd", course_section = "testc", meetings = "testm", component = "test", toggle = True, users = "user")
        response = self.client.get(reverse('SBfinder:class'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Instructor: Paul McBurney")

    

    