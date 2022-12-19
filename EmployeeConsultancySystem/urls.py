"""EmployeeConsultancySystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from employee.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

#from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('registration/', registration, name='registration'),
    path('emp_login/', emp_login, name='emp_login'),
    path('emp_home/', emp_home, name='emp_home'),
    path('profile/', profile, name='profile'),
    path('logout/', Logout, name='logout'),
    path('admin_login/', admin_login, name='admin_login'),
    path('my_experience/', my_experience, name='my_experience'),
    path('edit_myexperience/', edit_myexperience, name='edit_myexperience'),
    path('my_education/', my_education, name='my_education'),
    path('edit_myeducation/', edit_myeducation, name='edit_myeducation'),
    path('change_password/', change_password, name='change_password'),
    path('admin_home/', admin_home, name='admin_home'),
    path('change_passwordadmin/', change_passwordadmin, name='change_passwordadmin'),
    path('all_employee/', all_employee, name='all_employee'),
    path('my_resume/', my_resume, name='my_resume'),
    path('edit_myresume/', edit_myresume, name='edit_myresume'),
    path('forgotten_password/', forgotten_password, name='forgotten_password'),
    path('termsandcondition/', termsandcondition, name='termsandcondition'),
    path('job_training/', job_training, name='job_training'),
    path('help/', help, name='help'),
    path('apply/', apply, name='apply'),
    path('profileshow/', profileshow, name='profileshow'),
    path('qrcode/', qrcode, name='qrcode'),





]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



