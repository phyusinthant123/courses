from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..models import Feedback,Student
from ..forms import FeedbackForm

@login_required(login_url='/login')
def feedback(request):    
    form =FeedbackForm()
    if request.method == "POST":
        form =FeedbackForm(request.POST)
        if form.is_valid():            
            form.save()
            return redirect('/')

    return render(request,'feedback/feedbacks.html', {'form':form})


