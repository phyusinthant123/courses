from django.db import models
from.students import Student

class Feedback(models.Model):
    message=models.CharField(max_length=200,null=True)
    student=models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)

    def __str__ (self):
        return self.student.name
