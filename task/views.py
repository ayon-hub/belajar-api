from django.shortcuts import render
from django.http import JsonResponse
from . import models
# Create your views here.
def halloworld(request):
    belajar = models.Belajar.objects.all()
    html = list(belajar)
    
    return JsonResponse({'html':html})