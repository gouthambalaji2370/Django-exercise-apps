from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def display(request):
    return HttpResponse("<h1>my first django app</h1>")

def displayDateTime(request):
    dt=datetime.datetime.now();
    s="<b> current date and time: </b>"+str(dt)
    return HttpResponse(s);