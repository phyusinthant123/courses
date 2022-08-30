from mycourse.decorators import adminOnly
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from ..models import Student,Course,Attendence,Teacher


@login_required(login_url='/login')
@adminOnly
def dashboard(request):
    students=Student.objects.all()
    courses=Course.objects.all()
    attend=Attendence.objects.all()
    teachers=Teacher.objects.all()
    
    total_c=courses.count()
    total_s=students.count()
    total_atten=attend.count()

    return render(request,'dashboard.html',{
        'students':students,
        'courses':courses,
        'total_c':total_c,
        'total_s':total_s,
        'total_atten':total_atten,
        'teachers' :teachers,
        
    })