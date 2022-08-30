"""courseapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.dashboard,name='dashboard'),
    path('student/<int:id>',views.students,name='students'),
    path('student/student_profile/',views.student_profile,name='students.student_profile'),
    path('student_profile/setting/',views.student_profile_setting,name='students.student_profile_setting'),   
    path('register/',views.register,name='register'),
    path('login/',views.userLogin,name='login'),
    path('login/logout/',views.userLogout,name='logout'),    
    path('courses/',views.courses,name='courses'),
    path('course_create/',views.courseCreate,name='course_create'),
    path('course_update/<int:course_id>',views.course_update,name='course_update'),
    path('course_delete/<int:course_id>',views.course_delete,name='course_delete'),
    path('student_delete/<int:student_id>',views.student_delete,name='student_delete'),
    path('attendence/<int:course_id>',views.attendence,name='attendence'),
    path('attendence_update/<int:attendence_id>',views.attendence_update,name='attendence_update'),
    path('feedback/',views.feedback,name='feedback'),
    path('teacher/',views.createTeacher,name='teacher'),
    path('teacher_update/<int:teacher_id>',views.teacher_update,name='teacher_update'),
    path('teacher_delete/<int:teacher_id>',views.teacher_delete,name='teacher_delete'),

]
