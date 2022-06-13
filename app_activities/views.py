from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from app_user.models import UserProfileInfo
from django.http import HttpResponseRedirect
from django.urls import reverse
from importlib import import_module

import requests

from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError


def search(username):
    # INSTAGRAM
    instagram = f'https://www.instagram.com/{username}'

    # FACEBOOK
    facebook = f'https://www.facebook.com/{username}'

    # TWITTER
    twitter = f'https://www.twitter.com/{username}'


    # BADOO
    badoo = f'https://www.badoo.com/en/{username}'


    ''' WEBSITE LIST - USE FOR SEARCHING OF USERNAME '''
    WEBSITES = [
        facebook, instagram, twitter, badoo
    ]
    urls = []
    count = 0
    for url in WEBSITES:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                urls.append(url)
            count += 1
        except (ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError):
            continue
    return urls


def home_update(request):
    contents = '''There are number of social network sites that connect
					a large amount of people around the world. All social networking
					sites differ from each other based on various components such as
					Graphical User Interface, functionality, features etc. Many users
					have virtual identities on various social network sites.It is
					common that people are users of more than one social network and
					also their friends may be registered on multiple social network sites.
					User may login to different social networking sites at different
					timing, so user may not find his friends online when he logins to
					the particular social networking website.To overcome this issue our
					proposed system will bring together our online friends on different
					social networking sites into a single integrated environment.
					This would enable the user to keep up-to-date with their virtual
					contacts more easily, as well as to provide improved facility to
					search for people across different websites'''
    results = ''
    user = User.objects.get(pk=request.user.id)
    userProfile = UserProfileInfo.objects.filter(user_id=user.id)
    if request.method == "GET" and request.GET.get("username"):
        results = search(request.GET.get("username"))

    if request.method == "POST":
        if True:
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()
            userprofile = UserProfileInfo(user=request.user)
            userprofile.phone_no = request.POST['phone_no']
            userprofile.location = request.POST['location']
            userprofile.save()

            return HttpResponseRedirect(reverse('user_login'))
        else:
            print("an error occur")

    context = {
        "user": user,
        "userProfile": userProfile,
        "results": results,
        "contents": contents
    }
    return render(request, "app_activities/index.html", context)
