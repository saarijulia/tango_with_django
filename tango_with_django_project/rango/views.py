from django.shortcuts import render

from django.http import HttpResponse

#creating an view called index - takes in an HttpResponse object
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse("Rango says hey there partner!<a href='/rango/about/'>About</a> ")
# returning the HttpResponse object - sending this string to the content of the web

# Create your views here.

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Julia'}
    return render(request, 'rango/about.html', context=context_dict)