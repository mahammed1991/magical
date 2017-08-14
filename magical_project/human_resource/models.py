from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150, null=False)
    location = models.CharField(max_length=200, null=True, blank=True)
    total_employees = models.IntegerField(null=True, blank=True)
    company_description = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    recored_created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __unicode__(self):
    	return "%s | %s |%s" % (self.name, self.location, self.total_employees)

class EmployeeDetails(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=150, null=False)
    age = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    record_created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __unicode__(self):
    	return "%s | %s | %s" % (self.company, self.name, self.role)

class JobOpenings(models.Model):
    associated_company = models.ForeignKey(Company)
    role_name = models.CharField(max_length=150, null=False)
    role_description = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    record_created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    
    def __unicode__(self):
        return "%s | %s" % (self.associated_company, self.role_name)
    
    
