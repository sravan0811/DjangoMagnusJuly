from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def home(request):
    data = {"name":"Sravan"}
    return render(request,'MyApp1/Home.html', context=data)

def help(request):
    return HttpResponse("<h1>This is the Help Page</h1>")

def contact(request):
    return HttpResponse("<h1>This is Contact Page</h1>")

def emp(request):
    emp_data = Employee.objects.all() # all the records are retrieved from database table
    data = {"employee":emp_data}
    return render(request,'MyApp1/Emp.html',context=data)


