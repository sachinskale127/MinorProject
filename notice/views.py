from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from datetime import date
from .forms import ImageForm
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
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form =ImageForm()
    params = {'form':form, 'image':image}
    return render(request, 'admin.html',params)

def calendar(request):
    return render(request, 'calendar.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def test(request):
    image = Image.objects.all()
    no_of_image = len(image)
    dates = date.today()
    # times = date.time
    times = datetime.datetime.now().strftime('%H:%M:%S')
    params = {'product': image, 'number': no_of_image, 'dates':dates, 'times':times}
    return render(request, 'test.html', params)

