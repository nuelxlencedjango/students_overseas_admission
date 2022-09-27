from dataclasses import fields
#from tkinter import Widget
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        #fields ="__all__"
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name')






class AgentsForm(ModelForm):
    profile_img =CloudinaryField()
    class Meta:
        model = PartnersDetails
        fields =('profile_img','phone') 
        Widget ={
             'phone':forms.TextInput(attrs={'class':'form-control'}),
            'profile_img':forms.TextInput( attrs={'class':'form-control'}),
            #'country':forms.TextInput(attrs={'class':'form-control'}),
            }
            
    def __init__(self ,*args ,**kwargs):

        super(AgentsForm,self).__init__(*args ,**kwargs)
    






class PartnersLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')