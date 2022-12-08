
from django.urls import path
from .views import *
from . import views




app_name = 'core_app'
urlpatterns =[
    path('',views.homePage, name='home'),
    path('search_course/', views.search, name='search_course'),

     path('courses/', views.courseInformation, name='courses'),
     path('all_unis/', views.allOurUniversities, name='all_unis'),
     path('addmission_process/<int:id>/', views.submissionProcess, name='addmission_process'),

    path('course_selected/', views.confirmCourse, name='course_selected'),

    path('student_detail/', views.studentInformation, name='student_detail'),

    path('student_info/', views.studentApplicationDetails, name='student_info'),
    path('passport/<str:name>/',views.passportRegistration, name='passport'),
    path('addr/',views.studentAddr, name='addr'),
   path('emerge/',views.familyContact, name='emerge'),
   path('xp/',views.workX, name='xp'),


    path('student/',views.studentTable, name='student'),

     
      path('student_search/' , SearchResultsView.as_view() ,name="student_search"),
      
      path('uni_search/',views.universitySearch, name='uni_search'),

      path('universityDetail/<int:pk>/',views.universityImageGallery, name='universityDetail'),
      path('courseDetail/<int:pk>/',views.courseDetails, name='courseDetail'),
      
      path('selected_university/<int:pk>/',views.schoolChosen, name='selected_university'),

 
]

