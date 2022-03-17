from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sunny(request):
    return HttpResponse('sunny is cool')
def rahul(request):
    return HttpResponse('my friend')
