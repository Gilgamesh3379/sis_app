from django.contrib import admin

from webapp.models import UserProfile, CoursePrograms, Tuition

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CoursePrograms)
admin.site.register(Tuition)


