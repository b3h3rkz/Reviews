from django.contrib import admin
from .models import Student, Upload, Course, Level


class UploadsAdmin(admin.ModelAdmin):
    model = Upload
    list_display = ('title', 'upload_date', 'uploaded_by', 'level',)

class LevelsAdmin(admin.ModelAdmin):
    model = Level
    list_display = ('level', 'uploaded_files', 'id', )



class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('username', 'first_name', 'last_name', 'level',)


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('name', 'course_code', 'lecturer', 'level',)

admin.site.register(Upload, UploadsAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Level, LevelsAdmin)
admin.site.register(Course, CourseAdmin)
