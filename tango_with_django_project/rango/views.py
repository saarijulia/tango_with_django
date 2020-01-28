from django.shortcuts import render

from django.http import HttpResponse

#creating an view called index - takes in an HttpResponse object
def index(request):
    return HttpResponse("This is Julia's very cool web application!")
# returning the HttpResponse object - sending this string to the content of the web

# Create your views here.
