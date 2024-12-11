from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def list_todo_items(request):

    tasks = Task.objects.all()

    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    

    context ={'tasks':tasks,'form':form}

    return render(request,'todo/todolist.html',context)


def update_todo_items(request,pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        task = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')    

    context ={'task':task,'form':form}

    return render(request,'todo/todoupdate.html',context)


def delete_todo_items(request,pk):

    item = Task.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        return redirect('/')

    context ={'item':item}

    return render(request,'todo/tododelete.html',context)



