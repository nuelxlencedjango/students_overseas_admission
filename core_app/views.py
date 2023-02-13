
from django.shortcuts import render
from django.db.models import Q 
from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib import auth, messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView ,CreateView, UpdateView

from account.models import *

from .forms import *
from .forms import SchoolQualificationForm




def homePage(request):
    return render(request, 'base/base.html')




# course search 
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
    paginator = Paginator(course_item, 5)
    
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
            #email = form['studentEmail'].value()
            if form.is_valid():
                user = request.user
                info = form.save(commit=False)
                info.agent_name = user
                info.save()
                
                return redirect('core_app:student_detail')
              

            else:
                messages.info(request,f'Please select the appropirate intake time')  
                return redirect('core_app:courses')
                
    messages.info(request,'You need to register first.')          
    return redirect('account:login')





@login_required(login_url='/account/login')
def studentInformation(request):
    form = StudentAmissionForm()
    CourseSelection.objects.filter()
    if request.method =="POST":
        form = StudentAmissionForm(request.POST, request.FILES)
        if form.is_valid():
            email = request.POST.get('email')
            user = request.user
            info = form.save(commit=False)
            info.agent_name = user
            info.save()
            return redirect('core_app:passport',email)
        
        else:
            messages.info(request,'Wrong information.') 
             
            context ={'form':form}
            return render(request,'students/application.html',context)
            
    context ={'form':form}
    return render(request,'students/application.html',context)    




def passportInformation(request,email):
    if StudentAddmission.objects.filter(email=email):
        student =StudentAddmission.objects.filter(email=email)
        form = StudentPassportForm()

        context ={'form':form, 'student':student}

        messages.warning(request,'Student details saved successfully saved')
        return render(request, 'students/passportform.html',context)
         
    return render(request, 'students/passportform.html',context={"notFound":'No information found'})




def passportRegistration(request):
    form2 = StudentPassportForm(request.POST,request.FILES)    
    if request.method == 'POST':
        form2 = StudentPassportForm(request.POST,request.FILES)
      
        if form2.is_valid(): 
            passport = form2.save(commit=False)
            passport.agent_name = request.user

            email =request.POST.get('email')
            passport.save()

            return redirect('core_app:addr',email)
        
        else:
            messages.warning(request,'Form not submitted because of some mistake(s) in the form')
            context={'form2':form2}
       
            return render(request, 'students/passportform.html',context)
    

    
    context={'form2':form2}
    return render(request, 'students/passportform.html',context)





def studentAddr(request,email):
    form = StudentAddressForm()
    if StudentAddmission.objects.filter(email=email).exclude() and StudentPassort.objects.filter(email=email).exists():

        student =StudentPassort.objects.filter(email=email)
        context ={'form':form,'student':student}
        messages.warning(request,'passport details saved successfully saved')
        return render(request, 'students/addressform.html',context)
    
    messages.warning(request,'Student not found')
    return render(request, 'students/addressform.html')





def studentAddressRegister_view(request):

    form = StudentAddressForm(request.POST)
    if request.method == 'POST':
        form = StudentAddressForm(request.POST)
        if form.is_valid(): 
            addr = form.save(commit=False)
            addr.agent_name = request.user
            email =request.POST.get('email')
            addr.save()
            return redirect('core_app:emerge',email)
        
        else:
            messages.warning(request,'Form not submitted because of some mistake(s) in the form')
            context={'form':form}
       
        return render(request, 'students/addressform.html',context)

    
    return render(request, 'students/ddressform.html',context)





def familyContact(request,email):
    form = EmergencyContactForm()
    if StudentAddmission.objects.filter(email=email).exclude() and StudentPassort.objects.filter(email=email).exists() and StudentAddress.objects.filter(email=email).exists():

        student = StudentAddress.objects.filter(email=email)

        context ={'form':form,'student':student}
        messages.warning(request,'Address details saved successfully saved')
        return render(request, 'students/emergencyform.html',context)
        
    messages.warning(request,'Yser address information')    
    return redirect('/')




def emergencyContact(request):
        
        form = EmergencyContactForm(request.POST)
        if request.method == 'POST':
            form = EmergencyContactForm(request.POST)
            if form.is_valid(): 
                emergency = form.save(commit=False)
                emergency.agent_name = request.user
                emergency.save()
                email =request.POST.get('email')
                

                return redirect('core_app:work_xp',email)
        
        else:
            messages.warning(request,'Form not submitted because of some mistake(s) in the form')
            context={'form':form}
       
        return render(request, 'students/emergencyform.html',context)

    
    




def workX(request, email):
    form = WorkEXperienceForm()
    if StudentAddmission.objects.filter(email=email).exclude() and StudentPassort.objects.filter(email=email).exists() and StudentAddress.objects.filter(email=email).exists() and EmergencyContact.objects.filter(email=email).exists() :
        student = EmergencyContact.objects.filter(email=email)

        context ={'form':form,'student':student}
        messages.warning(request,'Alternative contacts saved successfully saved')
        return render(request, 'students/workform.html',context)
    
    messages.warning(request,'No alternative information given.')    
    return redirect('/')




def workExperience(request):
        form = WorkEXperienceForm(request.POST)
        if request.method == 'POST':
            form = WorkEXperienceForm(request.POST)
            if form.is_valid(): 
                xperience = form.save(commit=False)
                xperience.agent_name = request.user
                email =request.POST.get('email')
                xperience.save()

                return redirect('core_app:academic_info',email)
        
        else:
            messages.warning(request,'Information saved successfully.')
            context={'form':form}
       
        return render(request, 'students/academic.html',context)




class AcademicQualificationInline():
    form_class = SchoolQualificationForm
    model = SchoolQualification
    template_name = 'students/qualification.html'

    def form_valid(self,form):

        formsets = self.get_named_formsets()

        if not all(x.is_valid() for x in formsets.values() ):
            return self.render_to_response(self.get_context_data(form=form))
        
        self.object = form.save()
       
        SchoolQualification.objects.update(agent_name=self.request.user, fullName=form.cleaned_data['fullName'],email=form.cleaned_data['email'])
            
        for name,formset in formsets.items():
            formset_save = getattr(self, 'formset_{0}_valid'.format(name),None)
            if formset_save is not None:
                formset_save(formset)

            else:
                formset.save()

        return redirect("/") 
    
    
    def formset_variants_valid(self,formset):
        variants = formset.save(commit =False)
        for obj in formset.deleted_objects:
            obj.delete()

        for variant in variants:
            variant.product =self.object 
            variant.save()   


    def formset_images_valid(self,formset):  
        images =formset.save(commit= False)

        for obj in formset.deleted_objects:
            obj.delete()

        for image in images:
            image.academics =self.object
            image.save()             



class AcademicCreate(AcademicQualificationInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(AcademicCreate,self).get_context_data(**kwargs)

        student= StudentPassort.objects.get(email=self.kwargs.get('email'))
      
        ctx['student'] = student
        ctx['named_formsets'] =self.get_named_formsets()
        return ctx
    
    def get_named_formsets(self):
        if self.request.method =="GET":

            
            return {'variants': VariantsFormSet(prefix='variants'),
                    'images': ResultImageFormSet(prefix='images')
                    }
        else:
           
            return { 
                'variants':VariantsFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                'images' :ResultImageFormSet(self.request.POST or None, self.request.FILES or None, prefix ='images')
            }



class UpdateQualification(AcademicQualificationInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(UpdateQualification,self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()

        return ctx
    
    def get_named_formsets(self):
        return {
            'variants':VariantsFormSet(self.request.POST or None, self.request.FILES or None , instance=self.object, prefix ='variants'),
            'images': ResultImageFormSet(self.request.POST or None, self.request.FILES or None, instance = self.object, prefix='images')
        }


def delete_image(request, pk):

    try:
        image = ResultImage.objects.get(id=pk)
    except ResultImage.DoesNotExist:
        messages.success(request, "Image not found")   

        return redirect('core_app:academic_update', pk=image.academics.id) 
    
    image.delete()
    messages.success(request, 'successfully deleted')
    return redirect('core_app:academic_update', pk=image.academics.id)
    


def delete_variant(request,pk):
    try:
        variant = AdditionalQualification.objects.get(id=pk)

    except AdditionalQualification.DoesNotExist:
        messages.success(request,'Variant not found')
        return redirect('core_app:academic_update', pk=variant.product.id)
    

    variant.delete()
    messages.success(request,'successfully deleted')
    return redirect('core_app:academic_update', pk=variant.variant.product.id)





#work on this later

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

            email =request.POST.get('email')
            passport.save()

            return redirect('core_app:addr',email)
        


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

    def get_queryset(self):

        studentSearch ="Information"

        studId = self.request.GET.get('applicationId')
        studName = self.request.GET.get('firstName')
        studLast = self.request.GET.get('lastName')
        studEmail = self.request.GET.get('email')
       

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



