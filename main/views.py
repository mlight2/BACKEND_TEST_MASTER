from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Company, Employee
from .forms import *
from django.urls import reverse
# Create your views here.


def companies_view(request):
    return render(request, 'companies.html', {"companies": Company.objects.all()})


def add_employee_view(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            comment = form.cleaned_data['comment']
            company_name = form.cleaned_data['name']
            employee = Employee.objects.create(first_name=first_name, last_name=last_name, comment=comment)
            company = Company.objects.create(name=company_name,employees=employee)
            return redirect('/')
    else:
        form = AddEmployeeForm()

    return render(request, 'add_employee.html', {'form': form})

# def add_employee(request, company_id):
#     company = Company.objects.get(pk=company_id)
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             employee = form.cleaned_data['employee']
#             company.employees.add(employee)
#             return redirect(reverse('api:view_employee'))
#     else:
#         form = EmployeeForm()
#     return render(request, 'add_employee.html', {'form': form, 'company': company})
