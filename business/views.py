from business.models import Destination
from django.shortcuts import render

# Create your views here.


def index(request):
    dest1 = Destination()
    dest1.id = 1
    dest1.type = 'Graphics'
    dest1.desc = 'nice graphics'
    dest1.img = 'services-02.jpg'
    dest1.brand = 'branding'

    dest2 = Destination()
    dest2.id = 2
    dest2.type = 'UI/UX'
    dest2.desc = 'nice UI/UX'
    dest2.img = 'services-03.jpg'
    dest2.brand = 'graphic'
    # dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': [dest1, dest2]})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def pricing(request):
    return render(request, 'pricing.html')


def work(request):
    return render(request, 'work.html')


def worksingle(request):
    return render(request, 'work-single.html')
