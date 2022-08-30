from django.db import models


class Teacher(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    teacher_img=models.ImageField(null=True,blank=True,upload_to="static/img")
    
    def __str__ (self):
        return self.name

