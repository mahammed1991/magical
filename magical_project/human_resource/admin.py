from django.contrib import admin

# Register your models here.
from .models import Company, EmployeeDetails, JobOpenings

admin.site.register(Company)
admin.site.register(EmployeeDetails)
admin.site.register(JobOpenings)