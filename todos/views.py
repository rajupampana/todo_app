# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)
    # return HttpResponse('Hello todos')


def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        if title:
            print 'yes'
        try:
            if title or text:
                todo = Todo(title=title, text=text)
                todo.save()
        except Exception as e:
            print e
        # delete = request.POST['del']
        # ob = Todo.objects.get(title=title)
        # ob.delete()
        return redirect('/todos/')
    else:
        return render(request, 'add.html')


def delete(request, id=None):
    obj = Todo.objects.get(id=id)
    obj.delete()
    return redirect('/todos/')
