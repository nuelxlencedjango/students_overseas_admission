from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin


from .forms import *
from .models import User
from .models import *




# Register your models here.
admin.site.register(SchoolQualification)
admin.site.register(AdditionalQualification)
admin.site.register(ResultImage)

admin.site.register(StudentAddmission)
admin.site.register(CourseSelection)

admin.site.register(StudentApplication)
admin.site.register(StudentAddress)
admin.site.register(StudentPassort)
admin.site.register(WorkEXperience)

admin.site.register(EmergencyContact)
admin.site.register(CourseIntakeDate)
admin.site.register(Scholarship)
admin.site.register(UniversityAccommodation)


class CourseRequirementsAdmin(admin.StackedInline):
    model = CourseRequirements

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    inlines = [CourseRequirementsAdmin]

    class Meta:
       model = Courses

@admin.register(CourseRequirements)
class CourseRequirementsAdmin(admin.ModelAdmin):
    pass




class UniversityImageAdmin(admin.StackedInline):
    model = UniversityImages

@admin.register(Universities)
class UniversitiesAdmin(admin.ModelAdmin):
    inlines = [UniversityImageAdmin]

    class Meta:
       model = Universities

@admin.register(UniversityImages)
class UniversityImageAdmin(admin.ModelAdmin):
    pass





class CourseAdmin(admin.ModelAdmin):
    list_display =['courseName','duration','courseType','courseIntake','university','center','fees',
    'date_added','courseId']
    form =CourseSearchForm
    list_filter=['courseName'] 
    search_fields= ['courseName','courseType'] 



