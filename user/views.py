from django.shortcuts import render

def signup(request):
    return render(request, 'user/signup.html')

def login(request):
    return render(request, 'user/signup.html')
