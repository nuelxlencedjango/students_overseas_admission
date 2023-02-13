from email.mime import application
from email.policy import default
from django.db import models
from account.models import *
from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField
# Create your models here.
import datetime



class Courses(models.Model):
    courseName =  models.CharField(max_length=200, null=True)
    duration =  models.CharField(max_length=200, null=True)
    courseType =  models.CharField(max_length=200, null=True)
    #courseIntake =  models.CharField(max_length=200, null=True)
    university =  models.CharField(max_length=200, blank=True, null=True)
    center =  models.CharField(max_length=200, blank=True, null=True)
    fees = models.CharField(max_length=100, null=True)
    country =CountryField(blank=True,null=True)
    application_fees =models.CharField(max_length=50, null=True, blank=True)
    date_added =models.DateField(null=True,blank=True)
    courseId = models.CharField(max_length=200, null=True,blank=True)
    commission = models.DecimalField(max_digits=10,decimal_places=00,blank=True,null=True)
    why1 =models.CharField(max_length=900, null=True, blank=True)
    about =models.TextField(max_length=900, null=True,blank=True)
    overview =models.TextField(max_length=900, null=True,blank=True)
    detail =models.TextField(max_length=900, null=True,blank=True)

   

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
  courses =  models.ManyToManyField(Courses, null=True,blank=True,  related_name="university_courses")
  about =models.TextField(max_length=900, null=True,blank=True)
  overview =models.TextField(max_length=900, null=True,blank=True)
  description =models.TextField(max_length=900, null=True, blank=True)
  why1 =models.CharField(max_length=900, null=True, blank=True)
  type_of_university =models.CharField(max_length=20, null=True, blank=True)
  year_established =models.CharField(max_length=10, null=True, blank=True)
  type_of_institution =models.CharField(max_length=400, null=True, blank=True)
  number_of_students =models.CharField(max_length=400, null=True, blank=True)
 # application_fees =models.CharField(max_length=50, null=True, blank=True)
   
  
  class Meta:
    verbose_name_plural='Universities' 

  def __str__(self):
      return str(self.name)  



class CourseIntakeDate(models.Model):
  
  course =  models.ManyToManyField(Courses, null=True, related_name="course_date",blank=True)
  university =  models.ForeignKey(Universities,on_delete=models.SET_NULL, null=True, related_name="university_course_date",blank=True)
  winter_ApplicationDate =models.DateField(null=True,blank=True)
  winterApplicationDeadline =models.DateField(null=True,blank=True)
  winterStart_term_date =models.DateField(null=True,blank=True)
  winterEndStart_date =models.DateField(null=True,blank=True)
  summer_openApplicationDate =models.DateField(null=True,blank=True)
  summerDeadlineApplicationDate =models.DateField(null=True,blank=True)
  summerStart_term_date =models.DateField(null=True,blank=True)
  summerEndStart_date =models.DateField(null=True,blank=True)

  WinterIntakeTime=models.CharField(max_length=150, null=True, blank=True)
  summerIntakeTime=models.CharField(max_length=150, null=True, blank=True)

  def __str__(self):
      return f"{self.university.name} "



class Scholarship(models.Model):

  info =models.TextField(max_length=1500,blank=True,null=True)
  detail =models.TextField(max_length=1500,blank=True,null=True)
  img = CloudinaryField(blank=True,null=True)
  course =  models.ForeignKey(Courses, null=True,on_delete=models.SET_NULL, related_name="scholarshipInfo",blank=True)
  university =  models.ForeignKey(Universities,on_delete=models.SET_NULL, null=True, related_name="university_scholarship",blank=True)

  def __str__(self):
        return f"{self.course.courseName} - {self.university.name} "



class UniversityImages(models.Model):
    school=models.ForeignKey(Universities,on_delete=models.CASCADE)
    universityImages = CloudinaryField('images',blank=True,null=True)
   
    def __str__(self):
        return str(self.school)

    class Meta:
        #db_table='accommodation' 

        verbose_name_plural='University Images'          




class UniversityAccommodation(models.Model):
    school= models.ForeignKey(Universities,on_delete=models.SET_NULL, null=True, related_name="university_accommodation",blank=True)
    amount =models.CharField(max_length=50, null=True, blank=True)
    image = CloudinaryField('images',blank=True,null=True)
    description =models.TextField(max_length=600, null=True, blank=True)
    detail =models.TextField(max_length=600, null=True, blank=True)

   
    def __str__(self):
        return str(self.school)

    class Meta:
        #db_table='accommodation' 

        verbose_name_plural='University Accommodation' 





class CourseRequirements(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.SET_NULL, null=True, blank=True, related_name="university_requiremeents")
    university = models.ForeignKey(Universities,on_delete=models.SET_NULL, null=True,related_name="schools")
    requirement =  models.CharField(max_length=200, null=True)

    def __str__(self):
      return str(self.course)

    class Meta:
      verbose_name_plural='Course Requirements' 


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
  studentEmail = models.EmailField(max_length=200, null=False,blank=False)

  def __str__(self):
      return f"{self.agent_name} - {self.course_name}"
    

  class Meta:
      verbose_name_plural='Course Selection'


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
  phone = models.CharField(max_length=200, null=False)
  email = models.EmailField(max_length=200, null=False)
  dob =models.DateField(null=False,blank=False)
  application_date =models.DateField(null=True,blank=True)
  passport = CloudinaryField(blank=False,null=False)
  nationality =CountryField(blank=False, null=False)
  

  def __str__(self):
      #return str(self.firstName)
      return f"{self.agent_name} - {self.firstName} {self.lastName}"

  class Meta:
      verbose_name_plural='Student Addmission'





class StudentPassort(models.Model):
  
  agent_name = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='passportDetail')
  fullName =  models.CharField(max_length=200, null=False,blank=False)
  #lastName =  models.CharField(max_length=200, null=False,blank=False)
  email = models.EmailField(max_length=200, null=False,blank=False)

  passport_num =  models.CharField(max_length=200, null=False,blank=False)
  place_of_issue =  models.CharField(max_length=200, null=False,blank=False)
  place_of_birth = models.CharField(max_length=200,null=False,blank=False)
  date_issued =models.DateField(null=False,blank=False)
  expiry_date = models.DateField(null=True,blank=True)
  nationality =CountryField(null=False,blank=False)
  visa_denial =  models.BooleanField(default=False)
 

  def __str__(self):
      return f"{self.agent_name} - {self.fullName} "
      
  class Meta:
      verbose_name_plural='Student Passport'






#class UndergraduateApplication(models.Model):



class StudentApplication(models.Model):
  agent_name = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='application')
  firstName =  models.CharField(max_length=200, null=True)
  middleName =  models.CharField(max_length=200, null=True,blank=True)
  lastName =  models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=20, null=True)
  email = models.EmailField(max_length=200, null=True)
  dob =models.DateField(null=True,blank=True)
  application_date =models.DateField(null=True,blank=True)
  applicationId = models.CharField(max_length=200, null=True,blank=True)
  gender = models.CharField(max_length=20, null=True)
  nationality =CountryField(blank=True)


  def save(self, *args, **kwargs):
    if self.application_date is None:
      self.application_date = timezone.localtime(timezone.now())
      if self.applicationId is None:
        self.applicationId = str(uuid4()).split('-')[4]
   
      super(StudentApplication, self).save(*args, **kwargs)

  def __str__(self):
      return f"{self.agent_name} applied for {self.firstName}"

  class Meta:
      verbose_name_plural='Student Application'







class StudentAddress(models.Model):
  agent_name = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='address')
  fullName =  models.CharField(max_length=200, null=False,blank=False)
  email = models.EmailField(max_length=200, null=False,blank=False)
  street =  models.CharField(max_length=200, null=False,blank=False)
  street_two =  models.CharField(max_length=200, null=False,blank=False)
  city =  models.CharField(max_length=200, null=False,blank=False)
  state = models.CharField(max_length=200, null=False,blank=False)
  postal_code =models.CharField(max_length=200, null=True)
  nationality =CountryField(null=False,blank=False)
 


  def __str__(self):
      return f"{self.agent_name} -  {self.fullName}"

  class Meta:
      verbose_name_plural='Student Address'




class EmergencyContact(models.Model):
  agent_name = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE, related_name='contact')
  fullName =  models.CharField(max_length=200, null=True,blank=True)
  email = models.EmailField(max_length=200, null=True,blank=True)
  relationship =  models.CharField(max_length=200, null=True,blank=True)
  firstName =  models.CharField(max_length=200, null=True)
  lastName =  models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=200, null=True)
  relaticeEmail = models.EmailField(max_length=200, null=True)

 

  def __str__(self):
      return f"{self.agent_name} -  {self.fullName}"
  class Meta:
      verbose_name_plural='Emergency Contact'
  



class WorkEXperience(models.Model):
  agent_name = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='work')
  fullName =  models.CharField(max_length=200, null=True,blank=True)
  email = models.EmailField(max_length=200, null=True,blank=True)
  worked_before =  models.BooleanField(default=False)
  membership =  models.CharField(max_length=200, null=True,blank=True)
  employer =  models.CharField(max_length=200, null=True,blank=True)
  startDate =models.DateField(null=True,blank=True)
  endDate = models.DateField(null=True,blank=True)
  
  
  def __str__(self):
      return f"{self.agent_name} -  {self.fullName}"

  class Meta:
      verbose_name_plural='Work EXperience'




class SchoolQualification(models.Model):
  agent_name = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='academicsQualifications')
  fullName =  models.CharField(max_length=200, null=True,blank=True)
  email = models.EmailField(max_length=200, null=True,blank=True)
  sch_attended =  models.CharField(max_length=200, null=False,blank=False)
  state =  models.CharField(max_length=200, null=False,blank=False)
  country =CountryField(blank=True)
  startDate =models.DateField(null=False,blank=False)
  endDate = models.DateField(null=True,blank=True)
  certificate =  models.CharField(max_length=200, null=False,blank=False)
  
  
  def __str__(self):
     
      return f"{self.agent_name} -  {self.fullName}"

  class Meta:
      verbose_name_plural='Academic Qualification'      




class ResultImage(models.Model):
    academics = models.ForeignKey(SchoolQualification, on_delete=models.CASCADE, null=True )
    document = CloudinaryField('images',blank=True,null=True)
    title =  models.CharField(max_length=200, null=False,blank=False, default="school information")

    def __str__(self):
      
        return f"{self.academics.agent_name} - {self.academics.fullName} "
    



class AdditionalQualification(models.Model):
    product = models.ForeignKey(SchoolQualification, on_delete=models.CASCADE )
    sch_attended =  models.CharField(max_length=200, null=False,blank=False)
    state =  models.CharField(max_length=200, null=False,blank=False)
    country =CountryField(null=False,blank=True)
    startDate =models.DateField(null=False,blank=False)
    endDate = models.DateField(null=True,blank=True)
    certificate_obtained =  models.CharField(max_length=200, null=False,blank=False)

    def __str__(self):
     
        return f"{self.product.agent_name} -  {self.product.fullName}  "
    