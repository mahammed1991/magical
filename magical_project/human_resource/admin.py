from django.contrib import admin

# Register your models here.
from .models import Company, EmployeeDetails, JobOpenings

#admin functionality goes here

class EmployeeDetailsAdmin(admin.ModelAdmin):

    list_display = ('company','name','age','role')

#Below by registering we are telling to django to show in admin panal
admin.site.register(Company)
admin.site.register(EmployeeDetails,EmployeeDetailsAdmin)
admin.site.register(JobOpenings)