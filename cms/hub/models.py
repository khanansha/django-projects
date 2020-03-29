from django.db import models

# Create your models here.
class Homepost(models.Model):
    banner = models.ImageField(upload_to='hub/images', default="")
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70, default="")
    chead=models.CharField(max_length=50000,default="")

    def __str__(self):
         return self.title



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.name

class About(models.Model):
    post_id=models.AutoField(primary_key=True, default="")
    title=models.CharField(max_length=50,  default="")
    head=models.CharField(max_length=100, default="")
    chead=models.CharField(max_length=5000000, default="")

    def __str__(self):
        return self.title

class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True, default="")
    title=models.CharField(max_length=50, default="")
    chead=models.CharField(max_length=50000, default="")
    image=models.ImageField(upload_to='hub/image', default="")

    def __str__(self):
        return self.title





