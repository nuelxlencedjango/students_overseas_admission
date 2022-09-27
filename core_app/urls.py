
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

    path('addmission/', views.addmissionApplication, name='addmission'),
 
]

