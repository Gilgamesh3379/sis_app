from django.contrib import admin

from webapp.models import SISapp, Programs, Lecturers, Students, Parents, Courses, Marks

# Register your models here.
admin.site.register(SISapp)
admin.site.register(Programs)
admin.site.register(Lecturers)
admin.site.register(Students)
admin.site.register(Parents)
admin.site.register(Courses)
admin.site.register(Marks)

