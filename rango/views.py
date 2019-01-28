from django.shortcuts import render
from rango.models import Category, Page
from rango.forms import CategoryForm

# This code imports the HttpResponse object from django.http module.
from django.http import HttpResponse


# The code shows one of the individual part of the view called index, this is represented by a function.
def index(request):
    # Query the database for a list of All categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine

    category_list = Category.objects.order_by('-likes')[:5]
    # For pages

    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}

    # construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{boldmessage}} in the templates!

    # context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcakes!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the first template we wish to use
    # and the second is a template context- python dictionary.
    return render(request, 'rango/index.html', context_dict)


# About Method
def about(request):
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNot Exist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        # Adds our results list to the templates context under name pages.
        context_dict['pages'] = pages

        # We also add the category object form
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exist.
        context_dict['category'] = category
    except Category.DoesNotExist:

        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category " message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

        # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    form = CategoryForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            return index(request)
        else:
            # The supplied form contained errors
            # just print them to the terminal
            print(form.errors)

    # Will handle the bad form, or no form supplied cases
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})

