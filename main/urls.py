from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home_view, name='home'),
    path('dashboard/', views.homeView, name="dashboard"),
    path('profile/shantay', views.profileView, name="shantay"),
    path('profile/robert', views.RprofileView, name="robert"),
    path('metrices/', views.matrices, name="matrices"),
    path('about/', views.about, name="about"),   
    path('password-recovery/', views.homeView, name="recovery"),
    path('error/', views.error, name='error'),
    path('recover-pw/', views.reset, name = 'reset-pw'),
    path('', views.Home, name="home"),
    path('lets_go!/', views.success, name="filled"),
    path('criteria/', views.criteria, name="criteria"),
    path('services/', views.services, name="services"),
    path('education/', views.education, name="education"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('apply/', views.apply, name="apply"),
    path('principles/', views.principles, name="principles"),
]
