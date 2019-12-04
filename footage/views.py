import uuid

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from .forms import UploadFileForm
from .models import File

def detail(request, key):
    return HttpResponse(Footage.objects.filter(uuid=uuid.UUID(key)))
    return render(request, 'footage/detail.html')

def upload(request):
    upload_form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST)
        return JsonResponse(request.POST)
        if form.is_valid():
            return JsonResponse(request.POST)
        else:
            form = UploadFileForm(request.POST)
    
    context = {
        'upload_file_form': upload_form,
    }
    return render(request, 'footage/upload.html', context)
