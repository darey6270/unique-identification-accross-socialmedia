from django.urls import path
from . import views
app_name="app_activities"
urlpatterns = [
    path('home/', views.home_update, name="index"),
    # path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    # path('user_about/', views.AboutView.as_view(), name="about"),
]
