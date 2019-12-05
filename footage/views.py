import uuid
import json

from hurry.filesize import size

from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from .forms import UploadFileForm
from .models import File

def detail(request, key):
    footage_file = File.objects.get(uuid=uuid.UUID(key))

    footage_file_size = size(footage_file.footage_file.size)

    context = {
        'footage_file': footage_file,
        'footage_file_size': footage_file_size,
    }
    return render(request, 'footage/detail.html', context)

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
