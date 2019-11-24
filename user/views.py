from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import SignupForm

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
            )
            user.save()
            return JsonResponse(request.POST)
        else:
            form = SignupForm(request.POST)
    
    context = {
        'signup_form': form,
    }
    return render(request, 'user/signup.html', context)

def login(request):
    return render(request, 'user/login.html')