from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import AttendanceRecord,Students,Subjects

# Create your views here.
def homepage(request):
    if request.method=="POST":
        username = request.POST.get('Username')  # gets the value from input field
        password = request.POST.get('Password')
        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid credentials')

    return render(request,'Student/Home.html')

def loginpage(request):
    if request.method=="POST":
        username = request.POST.get('Username')  # gets the value from input field
        password = request.POST.get('Password')
        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid credentials')
    return render(request,'Student/Login.html')

def registeruser(request):
    if request.method=="POST":
        username=request.POST["Username"]
        password=request.POST["Password"]
        user=User.objects.create_user(username=username,password=password)
        user.save()
        return redirect('login')
    return render(request,'Student/Register.html')

def profilepage(request):
    return render(request,'Student/Profile.html')


def attendancepage(request):
    username = request.user
    student = Students.objects.get(username=username)  
    records = AttendanceRecord.objects.filter(student=student)  
    
    sub=list()
    total=dict()
    present=dict()
    for x in records:
        if x.subject.subjectname not in sub:
            sub.append (x.subject.subjectname)
            total[x.subject.subjectname]=1
            if x.status==0:
                present[x.subject.subjectname]=0
            else:
                present[x.subject.subjectname]=1
        else:
            total[x.subject.subjectname]=total[x.subject.subjectname]+1
            if x.status==1:
                present[x.subject.subjectname]=present[x.subject.subjectname]+1

    Data=list()
    for x in sub:
        per=float(present[x])/float(total[x])*100
        grade='None'
        if per>75:
            grade='Good'
        elif per>60:
            grade='Warning'
        else:
            grade='Low'
        Data.append ([x,total[x],present[x],per,grade])     

    enr=student.enrollment
    sem=student.semester
    brn=student.branch

    return render(request,'Student/Attendance.html',{'Data':Data,'Enroll':enr,'Semester':sem,'Branch':brn})

def logoutpage(request):
    logout(request)
    return redirect('home')