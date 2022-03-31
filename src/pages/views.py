from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *args, **kwargs):
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'home.html', {}) # 3rd arg = context


def contact_view(request, *args, **kwargs):
    print(request.user)
    return render(request, 'contact.html', {}) # 3rd arg = context


def about_view(request, *args, **kwargs):
    my_context = {
        "my_header": "playing with headers",
        "my_title": "This is about me",
        "my_number": 1234,
        "my_list": [1,2,3]
    }
    return render(request, 'about.html', my_context) # 3rd arg = context