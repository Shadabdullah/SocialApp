from email.policy import default
import imp
from statistics import mode
from django.db import models
from django.conf import settings
from django.conf.urls.static import static

# Create your models here.

class Profile(models.Model):
    id_user = pass
    pasword = pass
    bio = pass
    profileimage = models.ImageField(upload_to ="profile_image",default=)
    location = pass
    

