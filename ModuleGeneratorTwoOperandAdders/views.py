import buffer as buffer
from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse


from .Functions.CarryLA import CarryLookAhead
from .Functions.Test import RippleCarry
from .Functions.carrySelect import CarrySelect

def home_page(request):
    if request.method == "GET":
        return render(request, "../templates/home_page.html")

    elif request.method == "POST":
        if request.POST.get("SelectTypeOfAdder") == "Carry Look Aheaed Adder":
            CarryLookAhead(int(request.POST.get("DigitOfAdder")), str(request.POST.get("FilePath")))
        elif request.POST.get("SelectTypeOfAdder") == "Carry Ripple Adder":
            RippleCarry(int(request.POST.get("DigitOfAdder")), str(request.POST.get("FilePath")))
        elif request.POST.get("SelectTypeOfAdder") == "Carry Select Adder":
            CarrySelect(int(request.POST.get("DigitOfAdder")), str(request.POST.get("FilePath")))

        return render(request, "../templates/home_page.html")




def about_us_page(request):
    return render(request, "../templates/about_us.html")
