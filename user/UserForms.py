from django import forms
from django.contrib.auth.models import User
from .models import  profile
from django.contrib.auth.forms import UserCreationForm



# Creating a custom forms

class UserRegistration(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name','password1', 'password2']
class UserUpdate(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model  = User
        fields = ["email", 'first_name','last_name']

class UpdatePhoto(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['profile_image']

