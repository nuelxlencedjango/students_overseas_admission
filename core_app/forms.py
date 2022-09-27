

from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets


from .models import *




class CourseSearchForm(forms.ModelForm):
    class Meta:
        model=Courses
        fields =['courseName','courseType'] 




class StudentAmissionForm(forms.ModelForm):
    firstName = forms.CharField(label="First Name")
    middleName = forms.CharField()
    lastName = forms.CharField()
    
    email = forms.EmailField()
    phone = forms.CharField()
    dob = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
  
    passport =CloudinaryField()
    nationality = CountryField()

    class Meta:
        model = StudentAddmission
        fields =('firstName','middleName','lastName','email','phone','dob',
        'passport','nationality') 




        Widget ={
          
            'firstName':forms.TextInput( attrs={'class':'form-control','placeholder':'First Name'}),
            'middleName':forms.TextInput( attrs={'class':'form-control'}),
            'lastName':forms.TextInput( attrs={'class':'form-control'}),
            'email':   forms.EmailInput( attrs={'class':'form-control'}),
            'dob':forms.DateInput( attrs={'class':'form-control','type':'date'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            
            'passport':forms.FileInput( attrs={'class':'form-control'}),
            'nationality':forms.TextInput( attrs={'class':'form-control'}),
            #'country':forms.TextInput(attrs={'class':'form-control'}),
            }
            
    def __init__(self ,*args ,**kwargs):

        super(StudentAmissionForm,self).__init__(*args ,**kwargs)
        self.fields['nationality'].empty_label ="select country"




class CourseSearchForm(forms.ModelForm):
    class Meta:
        model=Courses
        fields =['courseName','courseType']         







class CourseSelectioForm(forms.ModelForm):
    class Meta:
        model=CourseSelection
        fields =('university','course_name','duration','course_type','course_intake','fees') 
