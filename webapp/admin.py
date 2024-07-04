from django.contrib import admin

from webapp.models import Students, Parents, Lecturer,CoursePrograms, Tuition, Marks

# Register your models here.
admin.site.register(Students)
admin.site.register(Parents)
admin.site.register(Lecturer)
admin.site.register(CoursePrograms)
admin.site.register(Tuition)
admin.site.register(Marks)

