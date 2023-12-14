"""
URL configuration for overseer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from leave_in_good_hands import views

urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('form/', views.DonationView.as_view(), name='form'),
    path('confirmation/', views.Confirmation.as_view(), name='confirmation'),
    path('profile/', views.UserProfile.as_view(), name='user_profile'),

]