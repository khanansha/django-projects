from django.shortcuts import render
from django.http import HttpResponse
from .models import About,Contact,Homepost
from math import ceil
# Create your views here.
def home(request):
    products = Homepost.objects.all()
    print(products)
    n = len(products)
    nSlides = n//1 + ceil((n/1)-(n//1))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'hub/home.html', params)


def about(request):
    mypost=About.objects.all()
    return render(request,'hub/about.html',{'mypost':mypost})

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        contact = Contact(name=name, email=email, phone=phone)
        contact.save()
    return render(request, 'hub/contact.html')

def blogpost(request,id):
    post = About.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'hub/blogpost.html',
                  {'post':post})


    