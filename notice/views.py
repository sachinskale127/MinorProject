from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, newsfeed, currentevent
from datetime import date
from .forms import ImageForm, newsfeedForm, currenteventForm
import datetime

def index(request):
    image = Image.objects.all()
    no_of_image = len(image)
    params = {'product': image, 'number': no_of_image}
    return render(request, 'index.html', params)

def administrator(request):
    image = Image.objects.all()
    # img = Image.photo
    if request.method == 'POST':
        form1 = ImageForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
    form1 =ImageForm()

    if request.method == 'POST':
        form2 = newsfeedForm(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
    form2 =newsfeedForm()

    if request.method == 'POST':
        form3 = currenteventForm(request.POST, request.FILES)
        if form3.is_valid():
            form3.save()
    form3 =currenteventForm()

    params = {'form1':form1, 'form2':form2,'form3':form3, 'image':image}
    return render(request, 'admin.html',params)

def calendar(request):
    return render(request, 'calendar.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def test(request):
    image = Image.objects.all()
    current = currentevent.objects.all()
    news = newsfeed.objects.all()

    no_of_image = len(image)
    dates = date.today()
    # times = date.time
    times = datetime.datetime.now().strftime('%H:%M:%S')
    params = {'product': image, 'number': no_of_image, 'dates':dates, 'times':times, 'currentevents':current, 'newsfeed':news}
    return render(request, 'test.html', params)

def add_show(request):
    return render(request, 'enroll/addandshow.html')