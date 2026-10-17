from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> this is lp </h1>")

def staf(request):
    return HttpResponse("<h1> this is lp as a stafe</h1>")

