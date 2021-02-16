from django.contrib import admin

# Register your models here.
from .models import Image, currentevent, newsfeed

admin.site.register(Image)
admin.site.register(currentevent)
admin.site.register(newsfeed)


