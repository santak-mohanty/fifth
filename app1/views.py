from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<marquee><h1>Hello</h1></marquee>")

def tata(response):
    return HttpResponse("<marquee><h1>Tata</h1></marquee>")
