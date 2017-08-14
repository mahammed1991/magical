from django.shortcuts import render, HttpResponse
from .models import Company, EmployeeDetails , JobOpenings
import json

# Create your views here.

def index(request):
    """GET API for Landing Page"""
    compny = Company.objects.filter(is_active=True)
    employee_details = EmployeeDetails.objects.filter(is_active=True)
    job_openings = JobOpenings.objects.filter(is_active=True)
    return render(request, "index.html", {'compny':compny,'emp_info':employee_details,'job_openings':job_openings })


def data_maker(query,type_of_data, table):
    return_list = []
    for each in query:
        data_maker_dict = {}
        data_maker_dict['table'] = table
        data_maker_dict['unique'] = each.id
        data_maker_dict['type_of_data'] = type_of_data

        if table == 'job':
            data_maker_dict['name'] = each.role_name
            data_maker_dict['description'] = each.role_description
        elif table == 'employee':
            data_maker_dict['name'] = each.name
            data_maker_dict['description'] = "Working as a " + str(each.role)+ "at " + str(each.company.name) + " and Age is " + str(each.age)
            data_maker_dict['employee_role'] = each.role
        elif table == 'company':
            data_maker_dict['name'] = each.name
            data_maker_dict['description'] = each.company_description
        return_list.append(data_maker_dict)
    
    return return_list


def search_result(request):
    """GET API for Search result"""
    returing_data = []

    if request.GET.get('search_key'):
        if int(request.GET.get('search_job_opeings')) == 1 :  
            job_openings_query = JobOpenings.objects.filter(is_active=True, role_name__contains= str(request.GET.get('search_key')))
            returing_data = returing_data + data_maker(job_openings_query, "Job Openings", "job")
            
        if int(request.GET.get('search_employees_inf') ) == 1 :
            employee_info_query = EmployeeDetails.objects.filter(is_active=True, role__contains= str(request.GET.get('search_key')))
            returing_data = returing_data + data_maker(employee_info_query, "Employee Information", "employee")
        
        if int(request.GET.get('search_company_inf') ) == 1:
            compny_info_query = Company.objects.filter(is_active=True, name__contains= str(request.GET.get('search_key')))
            returing_data = returing_data + data_maker(compny_info_query, "Company", "company")

        if str(request.GET.get('filter_applied') ) == 'NO':
            job_openings_query = JobOpenings.objects.filter(is_active=True, role_name__contains= str(request.GET.get('search_key') ) )
            employee_info_query = EmployeeDetails.objects.filter(is_active=True, role__contains= str(request.GET.get('search_key') ) )
            compny_info_query = Company.objects.filter(is_active=True, name__contains= str(request.GET.get('search_key')))
            returing_data = returing_data + data_maker(job_openings_query, "Job Openings", "job") + data_maker(employee_info_query, "Employee Information", "employee") + data_maker(compny_info_query, "Company", "company")
        
        print returing_data

        resp = {'success':True, 'msg':'suceesfully processed', 'data':returing_data}
    else:
        resp = {'success':False, 'msg':'No search key given', 'data':returing_data}
    
    return HttpResponse(json.dumps(resp), content_type="application/json")

