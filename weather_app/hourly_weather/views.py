from django.shortcuts import render

# Create your views here.
def hourly_view(request, *args, **kwargs):
    return render(request, "hourly.html", {})
