from django.shortcuts import render,redirect

from ..models import Student,Feedback
from django.contrib.auth.decorators import login_required
from ..forms import *
from django.contrib.auth.models import User


@login_required(login_url='/login')
def students(request,id):
    students=Student.objects.get(id=id)  
    attendences=students.attendence_set.all()
    feedbacks=students.feedback_set.all()
    return render(request,'student/student.html',{
        'students':students,
        'attendences':attendences,
        'feedbacks':feedbacks,
        
    })
    
@login_required(login_url='/login')
def student_profile_setting(request):
    form=StudentProfile(instance=request.user.student)
    if request.method=="POST":
        form=StudentProfile(request.POST,request.FILES,instance=request.user.student)
        if form.is_valid():
            form.save()
            return redirect('/student/student_profile')    
    return render(request,'student/profile_setting.html',{
        'form':form
    })

@login_required(login_url='/login')
def student_profile(request):
    student=Student.objects.all()
    attendences=request.user.student.attendence_set.all()
    course=Course.objects.all()

    return render(request,'student/student_profile.html',{
        'student':student,
        'attendences':attendences,
        'course':course,
        
        
        
    })

@login_required(login_url='/login')
def student_delete(request,student_id):
    student=Student.objects.get(pk=student_id)
    if request.method=="POST":
        student.delete();
        return redirect('/');
    return render(request,'course/course_delete.html',{
       'student' :student
    })    

