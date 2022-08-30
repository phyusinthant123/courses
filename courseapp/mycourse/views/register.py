from ..forms import RegisterForm
from django.contrib.auth import login
from django.shortcuts import render,redirect
from ..models import Student
from django.contrib.auth.models import Group
from mycourse.decorators import authenticated_user


@authenticated_user
def register(request):
    form=RegisterForm();
    if request.method=="POST":
        form=RegisterForm(request.POST);
        if form.is_valid():            
           user=form.save();
           gp=Group.objects.get(name="student")
           user.groups.add(gp)
           Student.objects.create(user=user)
           login(request,user)
        return redirect('/');
    return render(request,'register.html',{
        'form':form
    })
    