from django.contrib import admin

# Register your models here.
from .models import Company, EmployeeDetails, JobOpenings

#admin functionality goes here

class EmployeeDetailsAdmin(admin.ModelAdmin):

    list_display = ('company','name','age','role')

admin.site.register(Company)
admin.site.register(EmployeeDetails,EmployeeDetailsAdmin)
admin.site.register(JobOpenings)