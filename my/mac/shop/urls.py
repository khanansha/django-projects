from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index , name="shop_home"),
    path("about/", views.about , name="aboutus"),
    path("contact/", views.contact , name="contact"),
    path("tracker/", views.tracker , name="trackern status"),
    path("search/", views.search , name="search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout , name="checkout"),
    
]