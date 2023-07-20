from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return HttpResponse("<marquee><h1>Hi</h1></marquee>")

def bye(request):
    return HttpResponse("<marquee><h1>Bye</h1></marquee>")