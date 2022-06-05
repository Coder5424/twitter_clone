from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']



class PostForm(forms.ModelForm):
    attrs = {'class': 'form-control w-100', 'id': 'contentsBox', 'rows': '3', 'placeholder': "What's happening?",}
    content = forms.CharField(widget=forms.Textarea(attrs=attrs))

    class Meta:
        model = Post
        fields = ['content']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']




