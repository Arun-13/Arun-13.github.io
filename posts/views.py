# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Posts
from forms import PostForm

from django.core.files import File
from django.http import HttpResponse,HttpRequest,Http404
from django.views.generic.edit import CreateView


# Create your views here.

def index(request):
     return render(request,'posts/index.html')

def add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'posts/form.html', {'form': form})


def view(request):
   
    posts = Posts.objects.all()[:10]
    contxt = {
        'Title':'Latest post',
        'posts':posts
        
    }
    return render(request,'posts/view.html',contxt)


def details(request,id):
    post = Posts.objects.get(id=id)
  
    contxt = {
        'post': post
        }
    return render(request,'posts/details.html',contxt)


def delete(request):
     post = Posts.objects.get(id=id)
     post.delete()
     return redirect(view)



