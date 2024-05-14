from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from core.models import (
    User
)
from core.forms import SignUpForm


# Class based views
class signin(View):
    def get(self, request):
        logout(request)
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email = email, password = password)
        print(user)
        if not user:
            messages.error(request, 'Log In failed, Please check credentials')
            return redirect('/login')
        user = User.objects.filter(email=user).first()
        login(request, user)
        messages.success(request, 'Log In succeed')
        return redirect('/user/')

# Function based views
def index(request):
    return render(request, 'index.html')

def signout(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        if form.is_valid():
            print(form)
            email = form.cleaned_data.get('email')
            form.cleaned_data['is_active'] = True
            user = form.save()
            if user:
                user.is_active = True
                user.save()
                messages.success(request, 'User created successfully')
                return redirect('/')
            messages.error(request, 'Problem with user creation')
            return redirect('register')
        print(form.errors.items())
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, error)
        return redirect('register')
    signup_form = SignUpForm()
    args = {}
    args['form'] = signup_form
    return render(request, 'register.html', args)