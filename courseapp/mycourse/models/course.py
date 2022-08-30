from django.db import models



class Course(models.Model):
    
    name=models.CharField(max_length=200,null=True)
    courseFee=models.FloatField(null=True)
    course_pic=models.ImageField(null=True,blank=True,upload_to="static/img")
    description=models.CharField(max_length=200,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    dutation=models.CharField(max_length=200,null=True)
    

    def __str__ (self):
        return self.name

