from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your tests here.
class GoogleLoginTests(TestCase):

    def set_up_class(self):
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

    
