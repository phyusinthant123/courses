from django.contrib import admin
from .models import Student,Teacher,Course,Attendence,Feedback

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user','name','email','phone']
admin.site.register(Student,StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name','phone']
admin.site.register(Teacher,TeacherAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','courseFee']
admin.site.register(Course,CourseAdmin)

class AttendenceAdmin(admin.ModelAdmin):
    list_display =['course']
admin.site.register(Attendence,AttendenceAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display =['message']
admin.site.register(Feedback,FeedbackAdmin)

