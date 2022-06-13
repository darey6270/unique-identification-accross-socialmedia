from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse


def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)


class UserProfileInfo(models.Model):
    CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # adding additional attributes
    location = models.CharField(max_length=100, blank=True)
    phone_no = models.IntegerField()
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name='Profile Picture', blank=True, null=True)
    gender = models.CharField(choices=CHOICES, max_length=10, default='Male')

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
