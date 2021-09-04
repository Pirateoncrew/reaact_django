from django.shortcuts import render
from django.http import HttpResponse

def hello_wordl(request):
    return HttpResponse('Hello')