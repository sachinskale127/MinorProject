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
