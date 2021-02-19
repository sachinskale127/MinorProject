from django import forms
from .models import Image, newsfeed, currentevent, User

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

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'})

        } 