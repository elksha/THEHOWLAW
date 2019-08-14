from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm, LogInForm, UserForm, SignUpForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import requests

import requests
import xmltodict
import chardet
import collections

# Create your views here.


def home(request):
    return render(request, 'home.html')


def search(request):
    query = request.GET.get('query')
    law_list = []
    param2 = 3
    keyword = query
    raw_data = requests.get(
        f'http://openapi.ccourt.go.kr/openapi/services/PrecedentSearchSvc/getPrcdntSearchInfo?ServiceKey=PgwbRmIwJL%2BKZTXceW%2Bygt2h%2B809EQBIHtvWDvNGPorpmyeSin5SeT1NcJv4B8XLHAJscP0RwwRXOc7uAUdKmg%3D%3D&pansiMatt={keyword}&panreType=0{param2}').content
    xmlObject = xmltodict.parse(raw_data)
    # for k in range(0, 100):
    number_list = []
    # for i in range(0, len(xmlObject['response']['body']['items']['item'])):
    for i in range(0, 3):
        number = xmlObject['response']['body']['items']['item'][i]['eventNum']
        print(number)
        number_list.append(number)
    for k in number_list:
        raw_data2 = requests.get(
            f'http://openapi.ccourt.go.kr/openapi/services/PrecedentSearchSvc/getPrcdntDetailInfo?ServiceKey=aSsGKoThyf2YjJ+v57ZJWnxgD0OMKY4iKjUMCg/RlngOziGK1mkHcB7hVIqlnyJoYVbbOS7fgvU2S7WAAhL1fA==&eventNum={k}&panreType=0{param2}').content
        xmlObject = xmltodict.parse(raw_data2)
        a = xmlObject['response']['body']['items']['item']['pansiMatt']
        law_list.append({"num": k, "content": a})
    print(law_list)
    return render(request, 'eachresult.html', {"query": query, "law_list": law_list})


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
def posting(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.name = request.user.get_username()

        post.save()

        return redirect('home')
    else:
        form = PostForm()

        return render(request, 'posting.html', {'form': form})


def detail(request, post_pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)

        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        return redirect('detail', post.pk)
    else:
        post = Post.objects.get(pk=post_pk)
        form = CommentForm()

        return render(request, 'detail.html', {'post': post, 'form': form})


@login_required
def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form})


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')


def mypage_customer(request):
    posts = Post.objects.all()
    totalCnt = Post.objects.filter(name=request.user).count()
    return render(request, 'mypage_customer.html', {'totalCnt': totalCnt})


def mypage_lawyer(request):
    return render(request, 'mypage_lawyer.html')


def mypage_school(request):
    return render(request, 'mypage_school.html')


def chatbot_menu(request):
    return render(request, 'chatbot_menu.html')


def about(request):
    return render(request, 'about.html')


def centerslink(request):
    return render(request, 'centerslink.html')


def detail_list(request):
    return render(request, 'detail_list.html')


def lawyer_chat(request):
    return render(request, 'room.html')

def centerchat(request):
    return render(request, 'centerchat.html')

def private(request):
    return render(request, 'registration/private.html')
