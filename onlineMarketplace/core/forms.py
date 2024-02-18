from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username',
        'class': 'w-full py-4 px-6 rounded-xl m-2'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'w-full py-4 px-6 rounded-xl m-2'
    }))


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username',
        'class': 'w-full py-4 px-6 rounded-xl m-2'
    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email Address',
        'class': 'w-full py-4 px-6 rounded-xl m-2'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'w-full py-4 px-6 rounded-xl m-2'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Re Enter Password',
        'class': 'w-full py-4 px-6 rounded-xl m-2'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
