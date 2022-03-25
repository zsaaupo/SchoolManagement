from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def classes(request):
    return render(request, "classes.html")