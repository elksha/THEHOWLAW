from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def centerslink(request):
    return render(request, 'centerslink.html')

def lawyerchat(request):
    return render(request, 'lawyerchat.html')

def centerchat(request):
    return render(request, 'centerchat.html')