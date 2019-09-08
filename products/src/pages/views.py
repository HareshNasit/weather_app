from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request,*args, **kwargs):
    print(request.user)
    return render(request, "home.html",{})

def contact_view(request,*args, **kwargs):
    my_context = { "Shoes": "Adidas",
                    "Size": 10,
                    "Types": ["Predator", "F50", "Ace", "X"]}
    return render(request, "contact_view.html",my_context)
