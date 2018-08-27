from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, Worker, User, Complains
import os

import base64
from django.core.files.base import ContentFile

# Create your views here.

def get_all_complaints(request):
    if request.method == 'GET':
        query = Complains.objects.values()
    return render(request, 'index.html', {'data': list(query)})

def frzi():
    # format, imgstr = query[0]['image'].split(';base64,')
    # ext = format.split('/')[-1]
    # data = base64.b64decode(imgstr)
    # # print(os.getcwd())
    # os.chdir('project/static/images/')
    # file_name = "image." + ext
    # with open(file_name, 'wb') as f:
    #     f.write(data)
    return True
