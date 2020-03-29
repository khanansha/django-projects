from django.db import models

# Create your models here.
class Jobs(models.Model):
    image=models.ImageField(upload_to='job/images' , default="")
    summary=models.CharField(max_length=500 , default="")
    title=models.CharField(max_length=50 , default="")
    post_id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.title


    

    

    



