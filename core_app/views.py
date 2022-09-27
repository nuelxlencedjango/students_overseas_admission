from multiprocessing import context
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



