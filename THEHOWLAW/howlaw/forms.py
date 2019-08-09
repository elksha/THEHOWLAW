from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'pwd', 'title', 'post', 'img',]

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
        fields = ('username', 'password')
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