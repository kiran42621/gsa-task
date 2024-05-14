from django.shortcuts import render, redirect
from core.models import (
    User,
    Task
)
from django.contrib import messages

import datetime

def dashboard(request):
    userlist = User.objects.all()
    tasklist = Task.objects.all()
    args = {}
    args['task'] = tasklist
    args['userlist'] = userlist
    return render(request, 'dashboard.html', args)

def addtask(request):
    if request.method == 'POST':
        print(request.POST)
        user = User.objects.get(email=request.POST['assigned_user'])
        if user:
            task = Task.objects.create(
                title=request.POST['name'],
                status='Assigned',
                datetime=datetime.datetime.now(),
                assigned_to= user
            )
            print(task)
            if task:
                messages.success(request, 'Task added successfully')
                return redirect('dashboard')
            messages.error(request, 'No user found')
            return redirect('dashboard')
        messages.error(request, 'Error while creating task')
        return redirect('dashboard')
    return redirect('dashboard')
