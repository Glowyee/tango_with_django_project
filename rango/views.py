from django.shortcuts import render

# This code imports the HttpResponse object from django.http module.
from django.http import HttpResponse


# The code shows one of the individual part of the view called index, this is represented by a function.
def index(request):
    return HttpResponse("Rango says hey there partner!")
