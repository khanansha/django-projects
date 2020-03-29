from django.urls import path
from poll.views import *

urlpatterns = [
    path('',index , name="polls_list"),
    path('<int:id>/details/',detail, name="details_list"),
    path('<int:id>/',poll, name="poll_list"),



]