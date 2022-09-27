from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin


from .forms import *
from .models import User
from .models import *




# Register your models here.
admin.site.register(Universities)
admin.site.register(StudentAddmission)
admin.site.register(CourseSelection)


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






class CourseAdmin(admin.ModelAdmin):
    list_display =['courseName','duration','courseType','courseIntake','university','center','fees',
    'date_added','courseId']
    form =CourseSearchForm
    list_filter=['courseNam'] 
    search_fields= ['courseName','courseType'] 


