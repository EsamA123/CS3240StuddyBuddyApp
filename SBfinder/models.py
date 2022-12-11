from django.db import models
from django.conf import settings #Foreign Key?

# Create your models here.

class UserInfo(models.Model):
    user_name = models.CharField(max_length = 200)
    user_email = models.EmailField(max_length = 254)
    correspond_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.user_name


