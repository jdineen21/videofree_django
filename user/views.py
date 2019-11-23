from django.shortcuts import render

from .forms import SignupForm

def signup(request):
    return render(request, 'user/signup.html')

def login(request):
    return render(request, 'user/login.html')
