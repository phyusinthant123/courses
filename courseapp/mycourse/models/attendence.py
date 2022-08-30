from django.db import models
from.students import Student
from.course import Course
from.teacher import Teacher

class Attendence(models.Model):
    payment=(
        ('Wave Money','Wave Money'),
        ('KBZ Pay','KBZ Pay'),
        ('Mobile Banking','Mobile Banking')
    )
    student=models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)
    teacher=models.ForeignKey(Teacher,null=True,on_delete=models.SET_NULL)
    course=models.ForeignKey(Course,null=True,on_delete=models.SET_NULL)
    payment_method=models.CharField(max_length=200,null=True,choices=payment)
    
    def __str__(self):
        return self.course.name