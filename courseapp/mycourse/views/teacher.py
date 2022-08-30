from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..models import Teacher

from ..forms import *

@login_required(login_url='/login')
def createTeacher(request):  
    if request.method=="POST":
        form=TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save();
            return redirect('/')
    else:
        form =TeacherForm()        
    return render(request,'teacher/create_teacher.html',{
        'form':form
    })

@login_required(login_url='/login')
def teacher_update(request,teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    form = TeacherForm(instance=teacher)
    if request.method=="POST":
        form=TeacherForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('/teachers' )
    return render(request,'teacher/teacher_update.html',{'form':form})

@login_required(login_url='/login')
def teacher_delete(request,teacher_id):
    teacher=Teacher.objects.get(pk=teacher_id)
    if request.method=="POST":
        teacher.delete();
        return redirect('/');
    return render(request,'teacher/teacher_delete.html',{
       'teacher' :teacher
    })  





