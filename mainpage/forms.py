
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import get_user_model
from django import forms

class RegisterUserForm(UserCreationForm):
    
    username = forms.CharField(max_length=100, label='Имя пользователя') 
    password1 = forms.CharField(max_length=20, label='Пароль')
    password2 = forms.CharField(max_length=20, label='Повторить пароль')
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label='Имя пользователя') 
    password = forms.CharField(max_length=20, label='Пароль')
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
