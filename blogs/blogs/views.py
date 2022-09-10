from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import BlogPost
from . forms import BlogForm


def home(request):
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/home.html', context)


def post_text(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)


def edit_post_text(request, post_id):
    #Edit an existing post text
    post = BlogPost.objects.get(id=post_id)
    post_text = post.text
    
    if request.method != 'POST':
        form = BlogForm(instance=post)  #prefill with current post
    else:  #POST data submitted
        form = BlogForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('post', post_id=post.id)
        
    context = {'post': post, 'post_text': post_text, 'form': form}
    return render(request, 'blogs/edit_post_text.html', context)


def new_post(request):
    """Add a new post"""
    if request.method != 'POST':
        #No data submitted, create a blank form
        form = BlogForm()
    else:
        #POST data submitted, process data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)
