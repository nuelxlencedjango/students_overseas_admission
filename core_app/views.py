import email
from multiprocessing import context
from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.db.models import Q 
from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib import auth, messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.db.models import Q 
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.views.generic import (
    ListView 
)
from account.models import *

from .forms import *




def homePage(request):
    return render(request, 'base/base.html')


def search(request):
    title ="Search"
    query = request.GET.get('search')
    course_search = Courses.objects.filter(Q(courseName__icontains=query)| Q(courseType__icontains=query)| Q(duration__icontains=query)|Q(fees__icontains=query))
    name_search = Universities.objects.filter(Q(name__icontains=query)| Q(city__icontains=query))


    if course_search or name_search:
        context ={'nameSearch':course_search,'name_search':name_search, 'title':title}
        return render(request,'base/search.html',context)

    else:
        messages.warning(request,'No school or course found.')
        return render(request,'base/search.html')
            



def courseInformation(request):
    title ="Search"

    course_item = Courses.objects.all()
    number  = Courses.objects.all().count()
    requirement = CourseRequirements.objects.all()
    uni = Universities.objects.all()

    #pagination
    page =request.GET.get('page', 1)
    paginator = Paginator(course_item, 10)
    
    try:
        courseItems = paginator.page(page)

    except PageNotAnInteger:
        courseItems = paginator.page(1)

    except EmptyPage:   
        courseItems = paginator.page(paginator.num_pages)     


    context={'title':title, 'course_item':courseItems, 'requirement':requirement,'number':number,'uni':uni}    
    return render(request,'university/courses.html',context) 





def allOurUniversities(request):
    courses = Courses.objects.all()
    uni = Universities.objects.all()

    uni_num = Universities.objects.all().count()
    course_num = Courses.objects.all().count()
    
    context ={"uni":uni, 'courses':courses,'uni_num':uni_num,'course_num':course_num}
    return render(request, 'university/universities.html',context)





#@login_required(login_url='/account/login')
def submissionProcess(request,id):
    course_info = Courses.objects.get(id=id)
    uni = Universities.objects.get(courses=course_info)
    form = StudentAmissionForm()
    context={'form':form,'course_info':course_info,'uni':uni}
    return render(request,'students/course_select.html',context)



@login_required(login_url='/account/login')
def confirmCourse(request):
    if PartnersDetails.objects.filter(user=request.user).exists():
        form = CourseSelectioForm()
        if request.method =="POST":
            form = CourseSelectioForm(request.POST)
            print(form['fees'])
            print(form.errors)
            if form.is_valid():
                user = request.user
                info = form.save(commit=False)
                info.agent_name = user
                info.save()

                return redirect('core_app:student_detail')

            else:
                messages.info(request,'Wrong information.')  
                return redirect('core_app:courses')
                
    messages.info(request,'You need to register first.')          
    return redirect('account:login')





@login_required(login_url='/account/login')
def studentInformation(request):
    form = StudentAmissionForm()

    if request.method =="POST":
        form = StudentAmissionForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            info = form.save(commit=False)
            info.agent_name = user
            info.save()

            return redirect('account:p_dashboard')

        else:
            messages.info(request,'Wrong information.') 
             
            context ={'form':form}
            return render(request,'students/application.html',context)
            
    context ={'form':form}
    return render(request,'students/application.html',context)    





@login_required
def studentApplicationDetails(request):
    form1 = ApplicationForm()
    form2 = StudentPassportForm()
    form3 = StudentAddressForm()
    form4 = EmergencyContactForm()
    form5 = WorkEXperienceForm()
    

    if request.method == 'POST':
        form1 = ApplicationForm(request.POST)
        form2 = StudentPassportForm(request.POST,request.FILES)
        form3 = StudentAddressForm(request.POST)
        form4 = EmergencyContactForm(request.POST)
        form5 = WorkEXperienceForm(request.POST)
       
       
        if form1.is_valid():
            email = form1.cleaned_data.get('email')
            name = request.POST.get('firstName')
           

            if StudentApplication.objects.filter(email=email).exists():
                messages.warning(request,'A user with that email or phone number already exist')
                return render(request, 'base/base.html')

            else:
                partner = form1.save(commit=False)
                partner.agent_name = request.user
                partner.save()
                return redirect('core_app:passport',name)

        elif form2.is_valid(): 
            passport = form2.save(commit=False)
            passport.agent_name = request.user
            passport.save()

            return redirect('core_app:addr')

        elif form3.is_valid(): 
            address = form3.save(commit=False)
            address.agent_name = request.user
            address.save()
            messages.warning(request,'Address saved')
            return redirect('core_app:emerge')

        elif form4.is_valid(): 
            emergency = form4.save(commit=False)
            emergency.agent_name = request.user
            emergency.save()
            messages.warning(request,'Emergeency contacts saved')
            return redirect('core_app:xp') 


        elif form5.is_valid(): 
            xperience = form5.save(commit=False)
            xperience.agent_name = request.user
            xperience.save()
            messages.warning(request,'Account created successfully')

            context ={'form':form1}

            return render(request, 'base2/index.html', context)
            
            

            
        else:
            messages.warning(request,'Information not valid')
            return redirect('/')

                

def passportRegistration(request,name):

    form = StudentPassportForm()
    context ={'form':form}
    messages.warning(request,'Student details saved successfully saved')
    return render(request, 'students/passportform.html',context)



def studentAddr(request):
    form = StudentAddressForm()
    context ={'form':form}
    messages.warning(request,'passport details saved successfully saved')
    return render(request, 'students/addressform.html',context)



def familyContact(request):
    form = EmergencyContactForm()
    context ={'form':form}
    messages.warning(request,'Address details saved successfully saved')
    return render(request, 'students/emergencyform.html',context)



def workX(request):
    form = WorkEXperienceForm()
    context ={'form':form}
    messages.warning(request,'Emergency contact saved successfully saved')
    return render(request, 'students/workform.html',context)



def studentTable(request):
    if StudentApplication.objects.filter(agent_name=request.user).exists():

        userStudents = StudentApplication.objects.filter(agent_name=request.user)
        context ={'students': userStudents}
        return render(request, 'students/students.html',context)




def studentSearch(request):
    studentSearch ="Information"
    studId = request.GET.get('applicationId')
    studName = request.GET.get('firstName')
    studLast = request.GET.get('lastName')
    studEmail = request.GET.get('email')
    
    userStudents = StudentApplication.objects.filter(agent_name=request.user)
    
    if StudentApplication.objects.filter(Q(applicationId__icontains=studId)).exists() or StudentApplication.objects.filter(Q(firstName__icontains=studName)).exists() or StudentApplication.objects.filter(Q(lastName__icontains=studLast)).exists() or StudentApplication.objects.filter(Q(email__icontains=studEmail)).exists():                                    
        student =  StudentApplication.objects.filter(Q(applicationId__icontains=studId)| Q(firstName__icontains=studName)| Q(lastName__icontains=studLast)| 
                    Q(email__icontains=studEmail),agent_name=request.user)
                 
        context ={'student': student,'studentSearch':studentSearch}
        return render(request, 'students/students.html',context) 

    errorMessage = "No student with such details"
    context={'errorMessage':errorMessage, 'studentSearch':studentSearch}
    return render(request, 'students/students.html',context)                                                                 




class SearchResultsView(ListView):
    model = StudentApplication
    template_name = "students/students.html"
    context_object_name = 'student'

    def get_queryset(self): # new

        studentSearch ="Information"

        studId = self.request.GET.get('applicationId')
        studName = self.request.GET.get('firstName')
        studLast = self.request.GET.get('lastName')
        studEmail = self.request.GET.get('email')
        print(studEmail)

        return StudentApplication.objects.filter(firstName__icontains=studName, lastName__icontains=studLast, email__icontains=studEmail, agent_name=self.request.user)#, applicationId=studId)
        



#university search
def universitySearch(request):
    countryform = StudentAmissionForm()
    uni = Universities.objects.all()
    course = Courses.objects.all()
   
    number  = Courses.objects.all().count()
    

    if request.method == 'POST':
        form = CourseSearchForm(request.POST or None)
     
        if form['courseName'].value() !="" and form['country'].value() !="":
            courseItems = Courses.objects.filter(courseName__icontains =form['courseName'].value(), country__icontains=form['country'].value())
            context={'uni':uni,'course':courseItems,'form':countryform,'course_item':courseItems,'number_courses':number,}     
            return render(request, 'university/uniSearch.html',context)
           
         

        elif form['country'].value() !="":
            if Courses.objects.filter(country__icontains=form['country'].value()).exists():
                courseItems = Courses.objects.filter(country__icontains=form['country'].value()).exists()
                context={'uni':uni,'course':courseItems,'form':countryform,'course_item':courseItems,'number_courses':number,}     
             
                
            else:
                print('no country found')
                messages.info(request, 'No country found')

        elif form['courseName'].value() !="":
            if Courses.objects.filter(courseName__icontains =form['courseName'].value()).exists():

                courseItems = Courses.objects.filter(courseName__icontains =form['courseName'].value())    
                #print('course:',form['courseName'].value())
                context={'uni':uni,'course':courseItems,'form':countryform,'course_item':courseItems,'number_courses':number,}     
                return render(request, 'university/uniSearch.html',context)
            else:
                print('not found')
                
        else:
            return render(request, 'university/uniSearch.html',context)
            
           
        #pagination
    page =request.GET.get('page', 1)

    paginator = Paginator(course, 5)
    pag = Paginator(uni, 2)

         
    try:
        if paginator or pag:
            courseItems = paginator.page(page)

    except PageNotAnInteger:

        courseItems = paginator.page(1)

    except EmptyPage:   
        courseItems = paginator.page(paginator.num_pages) 


    context={
         'uni':uni,
        'course':courseItems,
        'form':countryform,
        'course_item':courseItems,
        'number_courses':number,
       
        }  
    

    return render(request, 'university/uniSearch.html',context)




def courseDetails(request,pk):
   # school = get_object_or_404(Courses,pk=pk)
    uni_course =Courses.objects.filter(pk=pk)
    for d in uni_course:
        sch = d.university
        #c = d.scholarshipInfo
       
        

    name =Universities.objects.filter(name=sch)
    
    context={ 'name':name,'uni_course':uni_course}
    return render(request,'university/universityCourses.html',context)     





def universityImageGallery(request,pk):

    id = Courses.objects.filter(pk=pk)
   
    for school in id:   
        uni =school.university
        univeristy_courses = Courses.objects.filter(university_courses__name__contains=uni)
        if Universities.objects.get(name=uni):
            name =Universities.objects.get(name=uni)
            images = UniversityImages.objects.filter(school=name)
            number = len(images)
            no_of_courses = len(univeristy_courses)
           
        else:
            messages.info(request,'No school found')
      
       
        context={'images':images,'number':number,'university':name, 'univeristy_courses':univeristy_courses,'no_of_courses':no_of_courses} 
    return render(request,'university/universityDetails.html',context) 



def schoolChosen(request,pk):

    id = Universities.objects.filter(pk=pk)
    for school in id:   
        uni =school.name
        #univeristy_courses = Courses.objects.filter(university_courses__name__contains=uni)
        if Universities.objects.get(name=uni):
            name =Universities.objects.get(name=uni)

            univeristy_courses = Courses.objects.filter(university_courses__name__contains=uni)
            images = UniversityImages.objects.filter(school=name)
            number = len(images)
            no_of_courses = len(univeristy_courses)
           
        else:
            messages.info(request,'No school found')
      
       
        context={'images':images,'number':number,'university':name, 'univeristy_courses':univeristy_courses,'no_of_courses':no_of_courses} 
    return render(request,'university/universityDetails.html',context) 



