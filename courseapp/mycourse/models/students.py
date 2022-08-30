from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_pic=models.ImageField(null=True,blank=True,upload_to="static/profiles",default="static/profiles/default.png")
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username