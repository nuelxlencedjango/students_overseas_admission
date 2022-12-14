

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



#here
  

class ApplicationForm(forms.ModelForm):
    firstName = forms.CharField(label="First Name")
    middleName = forms.CharField()
    lastName = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    dob = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    gender = forms.CharField()
    nationality = CountryField()
   

    class Meta:
        model=StudentApplication
        fields =('firstName','middleName','lastName','phone','email','dob','gender','nationality') 

    def __init__(self,*args, **kwargs):
        super(ApplicationForm, self).__init__(*args,**kwargs)

        self.fields['nationality'].empty_label = "Select country"
       


class StudentPassportForm(forms.ModelForm):
    passport_num = forms.CharField()
    place_of_issue = forms.CharField()
    place_of_birth = forms.CharField()
    date_issued = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    expiry_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    visa_denial =forms.BooleanField()
    nationality = CountryField()

    class Meta:
        model=StudentPassort
        fields =('passport_num','place_of_issue','place_of_birth','date_issued','expiry_date','visa_denial','nationality') 



class StudentAddressForm(forms.ModelForm):
    street = forms.CharField()
    street_two = forms.CharField()
    city= forms.CharField()
    state = forms.CharField()
    postal_code= forms.CharField()
    nationality = CountryField()

    class Meta:
        model=StudentAddress
        fields =('street','street_two','city','state','postal_code','nationality') 




class EmergencyContactForm(forms.ModelForm):
    relationship = forms.CharField()
    firstName = forms.CharField()
    lastName= forms.CharField()
    phone = forms.CharField()
    email= forms.CharField()

    class Meta:
        model=EmergencyContact
        fields =('relationship','firstName','lastName','phone','email') 



class WorkEXperienceForm(forms.ModelForm):
    
  

    worked_before = forms.BooleanField()
    membership = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'placeholder': 'membership'}))
    employer = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'Employer'}))
    startDate = forms.DateField(required=False,widget=forms.widgets.DateInput(attrs={'type':'date'})) 
    endDate  = forms.DateField(required=False, widget=forms.widgets.DateInput(attrs={'type':'date'}))

    class Meta:
        model=WorkEXperience
        fields =('worked_before','membership','employer','startDate','endDate') 




class CourseSearchForm(forms.ModelForm):
    class Meta:
        model=Courses
        fields =['courseName','country'] 



class UniversitySearchForm(forms.ModelForm):
    class Meta:
        model=Universities
        fields =['country','name'] 