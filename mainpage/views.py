from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .forms import LoginUserForm, RegisterUserForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.


def index(request):
    return redirect('about')

class About(TemplateView):
    template_name = 'mainpage/index.html'
    
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    form = RegisterUserForm()

    return render(request, 'mainpage/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        print(request.POST)
        print(form.is_valid())
    form = RegisterUserForm()
    return render(request, 'mainpage/register.html', {'form': form})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'mainpage/register.html'
    success_url = reverse_lazy('about')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'mainpage/login.html'
    success_url = reverse_lazy('about')

def logout_user(request):
    logout(request)
    return redirect('about')

def login_error(request):
    messages.error(request, 'Ошибка входа через Google. Пожалуйста, попробуйте снова.')
    return redirect('about')