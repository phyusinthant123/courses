from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mycourse.decorators import authenticated_user


@authenticated_user
def userLogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Username and Password is incorrect! Please try again !')
            return redirect('/login')
    return render(request,'login.html')        


def userLogout(request):
    logout(request);
    return redirect('/login')    