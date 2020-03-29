from django.shortcuts import render
from poll.models import *
from django.http import *
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

def index(request):
    context={}
    questions=Question.objects.all()
    context['questions']= questions
    context['title']="polls"

    return render(request,'polls/index.html',context)    


def detail(request,id=None):
    context={}
    try:
        question=Question.objects.get(id=id)
    except:
        raise Http404    
    context['question']= question
  
    return render(request,'polls/details.html',context)  


def poll(request,id=None):
    if request.method=="GET":
        try:
            question=Question.objects.get(id=id)
        except:
            raise Http404 
        context={}   
        context['question']= question
  
        return render(request,'polls/poll.html',context)  

    if request.method=="POST":
        user_id=1
        print(request.POST)
        data=request.POST
        ret=Answer.objects.create(user_id=user_id,choice_id=data['choice'])
        if ret:
            return HttpResponse("your vote is done successfully")

        else:
            return HttpResponse("your vote is not  done successfully")    

