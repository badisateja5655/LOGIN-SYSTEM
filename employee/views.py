from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth import login,logout,authenticate

from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            EmployeeDetails.objects.create(user = user,empcode=ec)
            EmployeeExperience.objects.create(user = user)
            EmployeeEducation.objects.create(user = user)
            EmployeeResume.objects.create(user = user)


            error="no"

        except:
            error="yes"
    return render(request,'registration.html',locals())


def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            error="no"
        else:
            error="yes"
    return render(request,'emp_login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request,'emp_home.html')

def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetails.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation= request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        employee.gender = gender

        if jdate :
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error="no"

        except:
            error="yes"
    return render(request,'profile.html',locals())

def admin_login(request):
    return render(request,'admin_login.html')

def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')


    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    return render(request,'my_experience.html',locals())

def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
            error="no"

        except:
            error="yes"
    return render(request,'edit_myexperience.html',locals())


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')


    user = request.user
    education = EmployeeEducation.objects.get(user=user)

    return render(request,'my_education.html',locals())


def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schollclgpg = request.POST['schollclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schollclggra = request.POST['schollclggra']
        yearofpassingra = request.POST['yearofpassingra']
        percentagegra = request.POST['percentagegra']

        coursessc = request.POST['coursessc']
        schollclgssc = request.POST['schollclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        coursehsc = request.POST['coursehsc']
        schollclghsc = request.POST['schollclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        education.coursepg = coursepg
        education.schollclgpg = schollclgpg
        education.yearofpassingpg = yearofpassingpg
        education.company1duration = percentagepg

        education.coursegra = coursegra
        education.schollclggra = schollclggra
        education.yearofpassingra = yearofpassingra
        education.percentagegra = percentagegra

        education.coursessc = coursessc
        education.schollclgssc = schollclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        education.coursehsc = coursehsc
        education.schollclghsc = schollclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagessc = percentagehsc

        try:
            education.save()
            error="no"

        except:
            error="yes"
    return render(request,'edit_myeducation.html',locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
            else :
                error="not"

        except:
            error="yes"
    return render(request,'change_password.html',locals())

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
               login(request,user)
               error="no"
            else:
               error="yes"

        except :
            error="yes"
    return render(request,'admin_login.html',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')


def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""

    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
            else :
                error="not"

        except:
            error="yes"
    return render(request,'change_passwordadmin.html',locals())


def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeDetails.objects.all()
    return render(request,'all_employee.html',locals())


def my_resume(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    user = request.user
    resume = EmployeeResume.objects.get(user=user)

    return render(request,'my_resume.html',locals())


def edit_myresume(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    resume = EmployeeResume.objects.get(user=user)
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        graduation = request.POST['graduation']
        qualifications = request.POST['qualifications']

        address = request.POST['address']
        btechcgpa = request.POST['btechcgpa']
        experience = request.POST['experience']
        sscschool = request.POST['sscschool']

        sscgpa = request.POST['sscgpa']
        intercollegename = request.POST['intercollegename']
        intercollegegpa = request.POST['intercollegegpa']


        resume.name = name
        resume.age = age
        resume.graduation = graduation
        resume.qualifications = qualifications

        resume.address = address
        resume.btechcgpa = btechcgpa
        resume.experience = experience
        resume.sscschool = sscschool

        resume.sscgpa = sscgpa
        resume.intercollegename = intercollegename
        resume.intercollegegpa = intercollegegpa

        try:
            resume.save()
            error="no"

        except:
            error="yes"
    return render(request,'edit_myresume.html',locals())

def forgotten_password(request):

    return render(request,'forgotten_password.html')

def termsandcondition(request):
    return render(request,'termsandcondition.html')

def job_training(request):

    return render(request,'job_trainingbase.html')

def help(request):
    return render(request,'help.html')

def apply(request):
    return render(request,'apply.html')

def profileshow(request):
    return render(request,'profileshow.html')


def qrcode(request):
    return render(request,'qrcode.html')












