from django.shortcuts import render, HttpResponse
from datetime import datetime
from appname.models import Comtact
from django.contrib import messages
# Create your views here.


def index(request):
    # messages.success(request, 'this test message')
    # return HttpResponse("this is hime page")
    context = {
        "var" : "or hai ki hall "
    }

    if request.method == 'POST':
        value = request.POST.get('value')
        email = request.POST.get('email')
        pho = request.POST.get('pho')
        decs = request.POST.get('decs')
        comtact = Comtact(value=value, email=email, pho=pho, decs=decs, date=datetime.today())
        comtact.save()
        # messages.success(request, "Profile details updated.")
        messages.success(request, 'this test message')
    return render (request, 'home.html', context)

def services(request):
    return render (request, 'services.html')
def aout(request):
    return render (request, 'aout.html')
def cotact(request):
   
    # return HttpResponse("this is cotact page")
    return render (request, 'cotact.html')

