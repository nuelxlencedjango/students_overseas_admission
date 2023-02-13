
from django.urls import path
from .views import *
from . import views




app_name = 'core_app'
urlpatterns =[
    path('',views.homePage, name='home'),
    path('search_course/', views.search, name='search_course'),

     path('courses/', views.courseInformation, name='courses'),
     path('all_unis/', views.allOurUniversities, name='all_unis'),
    
     path('admission_process/<int:id>/', views.submissionProcess, name='admission_process'),

    path('course_selected/', views.confirmCourse, name='course_selected'),

    path('student_detail/', views.studentInformation, name='student_detail'),
         
    path('passport/<str:email>/',views.passportInformation, name='passport'),  
           
     path('passportReg',views.passportRegistration, name='passportReg'),      

     path('addr/<str:email>/',views.studentAddr, name='addr'),
          
    path('addrForm/',views.studentAddressRegister_view, name='addrForm'),
         
    path('emerge/<str:email>/',views.familyContact, name='emerge'),
     path('emergContact',views.emergencyContact, name='emergContact'),     


    path('work_xp/<str:email>/',views.workX, name='work_xp'),
         
    path('experience/',views.workExperience , name='experience'),    

      path('academic_info/<str:email>/', AcademicCreate.as_view(), name="academic_info"),



    path('student_info/', views.studentApplicationDetails, name='student_info'),
 
   
    path('student/',views.studentTable, name='student'),

     
      path('student_search/' , SearchResultsView.as_view() ,name="student_search"),
      
      path('uni_search/',views.universitySearch, name='uni_search'),

      path('universityDetail/<int:pk>/',views.universityImageGallery, name='universityDetail'),
      path('courseDetail/<int:pk>/',views.courseDetails, name='courseDetail'),
      
      path('selected_university/<int:pk>/',views.schoolChosen, name='selected_university'),

 
]

