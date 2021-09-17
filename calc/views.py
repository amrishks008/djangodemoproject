from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'Sruthi'})


def add(request):
    num1 = request.POST["num1"]
    num2 = request.POST["num2"]
    res = int(num1)+int(num2)
    return render(request, 'results.html', {'res': res})
