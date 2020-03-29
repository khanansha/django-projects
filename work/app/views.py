
from django.shortcuts import render
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Employee
from .serializer import EmployeeSerializer
#from app. serializers import EmployeeSerializer
from rest_framework import status
#from rest_framework.serializers import *
from rest_framework.views import APIView

class employeelist(APIView):
    def get(self,request):
        obj=Employee.objects.all()
        serializer=EmployeeSerializer(obj,many=True)
        return Response(serializer.data)

# Create your views here.
#@api_view(['GET','POST'])
#def emplist(request):
    #if request.method=='GET':
        #obj=Employee.objects.all()
        #serializer=EmployeeSerializer(obj,many=True)
        #return Response(serializer.data)

    #elif request.method=='POST':
        #serializer=EmployeeSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
           # return Response(serializer.data, status=status.HTTP_201_CREATED)  

       # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)    

    