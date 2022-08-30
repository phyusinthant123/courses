
from django.forms.models import ModelForm


from.models import Student,Course,Attendence,Teacher,Feedback

from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']   

class StudentProfile(ModelForm):
    class Meta:
        model=Student
        fields=['name','email','phone','profile_pic'] 

class CourseCreate(ModelForm):  
    class Meta:
        model=Course
        fields=['name','courseFee','description','dutation','course_pic']  

class AttendenceForm(ModelForm):
    class Meta:
        model=Attendence  
        fields=['student','teacher','course','payment_method']  

class FeedbackForm(ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'


class TeacherForm(ModelForm):
    class Meta:
        model=Teacher 
        fields='__all__'                    