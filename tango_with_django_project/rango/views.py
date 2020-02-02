from django.shortcuts import render

from django.http import HttpResponse

#creating an view called index - takes in an HttpResponse object
def index(request):
    return HttpResponse("Rango says hey there partner!<a href='/rango/about/'>About</a> ")
# returning the HttpResponse object - sending this string to the content of the web

# Create your views here.

def about(request):
   return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>")