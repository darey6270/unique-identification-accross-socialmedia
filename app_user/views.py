from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from .models import UserProfileInfo, Contact
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))


def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return HttpResponseRedirect(reverse('user_login'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app_user/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


class user_login(LoginView):
    template_name = 'app_user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('app_activities:index')


class HomeView(TemplateView):
    template_name = 'app_user/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # standards = Standard.objects.all()
        # teachers = UserProfileInfo.objects.filter(user_type='teacher')
        # context['standards'] = standards
        # context['teachers'] = teachers
        return context


class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'app_user/contact.html'


class AboutView(TemplateView):
    template_name = 'app_user/about.html'
