from django.shortcuts import render,redirect
from ..models import Course
from ..forms import CourseCreate 
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def courses(request):
    courses=Course.objects.all()
    return render(request,'course/course.html',{
        'courses':courses
    })

@login_required(login_url='/login')
def courseCreate(request):    
    if request.method == "POST":
        form =CourseCreate(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/courses')
    else:
        form =CourseCreate()
    return render(request,'course/courseCreate.html', {'form':form})

@login_required(login_url='/login')   
def course_update(request,course_id):
    course = Course.objects.get(id=course_id)
    form = CourseCreate(instance=course)
    if request.method=="POST":
        form=CourseCreate(request.POST,request.FILES,instance=course,)
        if form.is_valid():
            form.save()
            return redirect('/courses' )
    return render(request,'course/course_update.html',{'form':form})

@login_required(login_url='/login')    
def course_delete(request,course_id):
    course=Course.objects.get(id=course_id)
    if request.method=="POST":
        course.delete();
        return redirect('/courses');
    return render(request,'course/course_delete.html',{
        'course':course
    })





