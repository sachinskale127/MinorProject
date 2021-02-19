from django.db import models
from datetime import date

# Create your models here.
class Image(models.Model):
    img_id = models.AutoField
    img_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='userimage/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=256, default="")


    def __str__(self):
        return self.img_name


class newsfeed(models.Model):
    title = models.CharField(max_length=100, default="")
    news = models.CharField(max_length=1024, default="")

    def __str__(self):
        return self.title

class currentevent(models.Model):
        title = models.CharField(max_length=100, default="")
        event = models.CharField(max_length=1024, default="")

        def __str__(self):
            return self.title

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)

