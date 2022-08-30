from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..models import Course,Attendence
from ..forms import AttendenceForm

@login_required(login_url='/login')
def attendence(request,course_id):    
    course=Course.objects.get(id=course_id)    
    form=AttendenceForm(initial={'course':course})
    if request.method=="POST":        
        form=AttendenceForm(request.POST)        
        if form.is_valid():           
            form.save();

            return redirect('/')
    return render(request,'attendence/attendence.html',{
        'form':form,        
        
    })

@login_required(login_url='/login')
def attendence_update(request,attendence_id):
    attendence=Attendence.objects.get(id=attendence_id)
    form=AttendenceForm(instance=attendence)
    if request.method=="POST":
        form=AttendenceForm(request.POST,instance=attendence)
        if form.is_valid():
            form.save();
            return redirect('/')

    return render(request,'attendence/attendence_update.html',{
        'form': form
    })    
    
