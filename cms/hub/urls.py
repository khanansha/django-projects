
from django.urls import path 
from . import views


urlpatterns = [
    path("", views.home, name="index"),
    path("about/", views.about, name="aboutus"),
    path("contact/", views.contact, name="contact"),
    path("blogpost/<int:id>", views.blogpost, name="blogpost"),
]

    #path("blogpost/<int:id>", views.blogpost, name="blogHome")

