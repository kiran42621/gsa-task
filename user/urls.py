from django.urls import path
from user.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('addtask', addtask, name="addtask"),
]
