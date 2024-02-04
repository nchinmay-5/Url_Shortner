from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import random,string
from django.urls import reverse
# Create your views here.
def home(request):
    print("home2")
    return render(request,"index.html")

def send_data(request):
    if request.method == 'POST':
        posted = False
        original = request.POST['url']

        while posted == False:
            short = Url_generator()
            data = URL(original_url=original, short_url = short)
            try:
                print("try")
                data.save()
                posted = True
            except:
                pass
        context = {'data_entered':True,'original_url':original,'short_url':short}
        return render(request, "index.html", context)

def Url_generator():
    short = ''.join(random.choice(string.ascii_letters)
                    for x in range(10))
    return short


def urlRedirect(request,short_url = None):
    print("As")
    if request.method == 'POST':
        print("ass")
        short_url = request.POST['short_url']
        print(short_url)
        data = URL.objects.get(short_url=short_url)
        return redirect(data.original_url)
    else:
        return redirect("http://127.0.0.1:8000/home/")
