from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_code=models.CharField(max_length=10)
    department=models.CharField(max_length=20)
    score=models.IntegerField(max_length=10)
    date=models.DateTimeField()


    def __str__(self):
        return self.department