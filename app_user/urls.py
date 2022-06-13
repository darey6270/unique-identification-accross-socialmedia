from django.urls import path
from . import views

urlpatterns = [
    #path('', views.HomeView.as_view(), name="index"),
    #path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    #path('user_about/', views.AboutView.as_view(), name="about"),
    path('', views.user_login.as_view(), name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('register/', views.register, name="register"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]
