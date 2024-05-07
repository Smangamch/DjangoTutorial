

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "webApplication/index.html", )

def my_view(request):
    context = {
        'foo': 'bar',
        'baz': 'qux',
    }
    return render(request, 'my_template.html', context)

def REAPER(request):
    return HttpResponse("Sho dah!")

def greeting(request, name):
    return render(request,"webApplication/greeting.html", {"name": name.capitalize()})
