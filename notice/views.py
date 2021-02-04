from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from datetime import date
from .forms import ImageForm

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

