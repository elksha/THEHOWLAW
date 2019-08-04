from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'img', 'pwd', 'post',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'content' ,)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email', 'password',)
        widgets = {
            'password': forms.PasswordInput()
        }