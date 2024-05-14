from django.urls import path
from core.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name="index"),
    path('login', signin.as_view(), name="login"),
    path('logout', signout, name="signout"),
    path('register', register, name="register")
]
