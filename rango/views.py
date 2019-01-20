from django.shortcuts import render

# This code imports the HttpResponse object from django.http module.
from django.http import HttpResponse


# The code shows one of the individual part of the view called index, this is represented by a function.
def index(request):
    # construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{boldmessage}} in the templates!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcakes!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the first template we wish to use
    # and the second is a template context- python dictionary.
    return render(request, 'rango/index.html', context=context_dict)


# About Method
def about(request):
    return render(request, 'rango/about.html')
