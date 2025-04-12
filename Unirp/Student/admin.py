from django.contrib import admin
from .models import Students,Subjects,AttendanceRecord

# Register your models here.
admin.site.register(Students)
admin.site.register(Subjects)
admin.site.register(AttendanceRecord)