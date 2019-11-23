from django.shortcuts import render

from .forms import SignupForm

def signup(request):
    context = {
        'signup_form': SignupForm(auto_id=False)
    }
    return render(request, 'user/signup.html', context)

def login(request):
    return render(request, 'user/login.html')
