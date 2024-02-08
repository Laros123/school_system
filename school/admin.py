from django.contrib import admin
from .models import Teacher, Grade, Schedule, Student, Class, Subject

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Grade)
admin.site.register(Schedule)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Class)
