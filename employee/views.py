from django.shortcuts import render, HttpResponse
from django.contrib import employee

def home(request):
    return HttpResponse("home page")
