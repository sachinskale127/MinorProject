from django import forms
from .models import Image, newsfeed, currentevent

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

class newsfeedForm(forms.ModelForm):
    class Meta:
        model = newsfeed
        fields = '__all__'

class currenteventForm(forms.ModelForm):
    class Meta:
        model = currentevent
        fields = '__all__'        