from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, "../templates/home_page.html")



def about_us_page(request):
    return render(request, "../templates/about_us.html")