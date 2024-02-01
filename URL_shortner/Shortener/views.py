from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import random,string
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request,"index.html",)

def send_data(request):
    if request.method == 'POST':
        original = request.POST['url']
        short = ''.join(random.choice(string.ascii_letters)
                       for x in range(10))
        data = URL(original_url = original, short_url = short )
        data.save()
        context = {'data_entered':True,'original_url':original,'short_url':short}
        return render(request, "index.html", context)


def urlRedirect(request,short_url = None):
    if request.method == 'POST':
        short_url = request.POST['short_url']
    print(short_url)
    data = URL.objects.get(short_url=short_url)
    return redirect(data.original_url)