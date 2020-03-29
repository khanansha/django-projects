from django.contrib import admin
from .models import  Homepost , About,Contact

# Register your models here.
admin.site.register(Homepost)
admin.site.register(About)
admin.site.register(Contact)