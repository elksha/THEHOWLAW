from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm, LogInForm, UserForm, SignUpForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import requests

<<<<<<< HEAD
# Create your views here.
=======
def social(request):
    return render(request,'social.html')

>>>>>>> 94f487ba733b0ce921c4220d6c0c04a220b324d3
def home(request):
    return render(request, 'home.html')
        
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # new_user = User.objects.create_user(**form.cleaned_data)
            # auth.login(request, new_user)
            return redirect('login')
        else:
            form = SignUpForm()
            error = "아이디가 이미 존재합니다"
            return render(request, 'registration/signup.html', {'form': form, 'error': error})
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

@login_required
def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.name = request.user.get_username()

        post.save()

        return redirect('detail', post_pk = post.pk)
    else:
        form = PostForm()
        
        return render(request, 'new.html', { 'form' : form })

def detail(request, post_pk):
    if request.method == 'POST':
        post = Post.objects.get(pk = post_pk)

        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        return redirect('detail', post.pk)
    else:
        post = Post.objects.get(pk=post_pk)
        form = CommentForm()

        return render(request, 'detail.html', { 'post' : post, 'form' : form })

@login_required
def edit(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'edit.html', {'form' : form})

@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    post.delete()
    return redirect('home')

def mypage_customer(request):
    posts = Post.objects.all()
    totalCnt = Post.objects.filter(name=request.user).count()
    return render(request, 'mypage_customer.html', { 'totalCnt' : totalCnt })

def mypage_lawyer(request):
    return render(request, 'mypage_lawyer.html')

def mypage_school(request):
    return render(request, 'mypage_school.html')

def chatbot_menu(request):
    return render(request, 'chatbot_menu.html')

def menubar(request):
    return render(request, 'menubar.html')

def about(request):
    return render(request, 'about.html')

def centerslink(request):
    return render(request, 'centerslink.html')

def detail_list(request):
    return render(request, 'detail_list.html')

def lawyer_chat(request):
    return render(request, 'lawyerchat.html')

def room(request):
    return render(request, 'room.html')

