from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class employee(models.Model):
    name=models.CharField(max_length=30)
    lastname=models.CharField(max_length=50)
    dob=models.DateField(auto_now=True)

    def __str__(self):
        return self.name