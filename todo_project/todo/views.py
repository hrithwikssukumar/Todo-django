from django.shortcuts import render
from django.http import HttpResponse

def list_todo_items(request):
    return render(request,'todo/todolist.html')

def add_todo_items(request):
    pass

def delete_todo_items(request):
    pass



