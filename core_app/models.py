from email.mime import application
from django.db import models
from account.models import *
from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField
# Create your models here.




class Courses(models.Model):
    courseName =  models.CharField(max_length=200, null=True)
    duration =  models.CharField(max_length=200, null=True)
    courseType =  models.CharField(max_length=200, null=True)
    courseIntake =  models.CharField(max_length=200, null=True)
    university =  models.CharField(max_length=200, blank=True, null=True)
    center =  models.CharField(max_length=200, blank=True, null=True)
    fees = models.CharField(max_length=100, null=True)

    date_added =models.DateField(null=True,blank=True)
    courseId = models.CharField(max_length=200, null=True,blank=True)

    class Meta:
      verbose_name_plural='Courses'

    def __str__(self):
      return str(self.courseName)

    def save(self, *args, **kwargs):
      if self.date_added is None:
        self.date_added = timezone.localtime(timezone.now())
        if self.courseId is None:
          self.courseId = str(uuid4()).split('-')[4]
   
        super(Courses, self).save(*args, **kwargs) 

 

class Universities(models.Model):
  country =CountryField(blank=True)
  name =  models.CharField(max_length=200, null=True)
  img = CloudinaryField(blank=True,null=True)
  city = models.CharField(max_length=200, null=True)
  courses =  models.ManyToManyField(Courses, null=True, related_name="university_courses")
  
  class Meta:
    verbose_name_plural='Universities' 

  def __str__(self):
      return str(self.name)      



class CourseRequirements(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.SET_NULL, null=True,related_name="university_requiremeents")
    university = models.ForeignKey(Universities,on_delete=models.SET_NULL, null=True,related_name="schools")
    requirement =  models.CharField(max_length=200, null=True)

    def __str__(self):
      return str(self.course)

    class Meta:
      verbose_name_plural='CourseRequirements' 


#user actions

class CourseSelection(models.Model):

  agent_name = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='selectCourse')
  university =  models.CharField(max_length=200, null=True)
  course_name =  models.CharField(max_length=200, null=True)
  duration =  models.CharField(max_length=200, null=True)
  course_type =  models.CharField(max_length=200, null=True)
  course_intake =  models.CharField(max_length=200, null=True)
  fees = models.CharField(max_length=100, null=True)
  selection_date =models.DateField(null=True,blank=True)
  status = models.CharField(max_length=200, null=True,blank=True,default='course selected')
  selectionId = models.CharField(max_length=200, null=True,blank=True)
  applied = models.BooleanField(default=False,blank=True,null=True)

  def __str__(self):
      return f"{self.agent_name} - {self.course_name}"
    

  class Meta:
      verbose_name_plural='CourseSelection'


  def save(self, *args, **kwargs):
    if self.selection_date is None:
      self.selection_date = timezone.localtime(timezone.now())
      if self.selectionId is None:
        self.selectionId = str(uuid4()).split('-')[4]
   
      super(CourseSelection, self).save(*args, **kwargs)     



class StudentAddmission(models.Model):
  agent_name = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='student_information')
  firstName =  models.CharField(max_length=200, null=True)
  middleName =  models.CharField(max_length=200, null=True,blank=True)
  lastName =  models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=200, null=True)
  email = models.EmailField(max_length=200, null=True)
  dob =models.DateField(null=True,blank=True)
  application_date =models.DateField(null=True,blank=True)
  passport = CloudinaryField(blank=True,null=True)
  nationality =CountryField(blank=True)

  def __str__(self):
      return str(self.firstName)

  class Meta:
      verbose_name_plural='StudentAddmission'


#class UndergraduateApplication(models.Model):
  


