from django.shortcuts import render

def detail(request):
    return render(request, 'footage/detail.html')
