from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee,Car
from .forms import UserForm,EmpForm
from rest_framework import viewsets
from .serializers import CarSerializer
# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('Brand')
    serializer_class = CarSerializer


def home(request):
    return render(request,'MyApp1/base.html')

def help(request):
    return HttpResponse("<h1>This is the Help Page</h1>")

def contact(request):
    return HttpResponse("<h1>This is Contact Page</h1>")

def emp(request):
    emp_data = Employee.objects.all() # all the records are retrieved from database table
    data = {"employee":emp_data}
    return render(request,'MyApp1/Emp.html',context=data)

def form_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['user'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['password'])
    return render(request,'MyApp1/UserForm.html',{'form':form})

def emp_formpage(request):
    form = EmpForm()
    if request.method=='POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h1>Inserted Successfully</h1>")
        else:
            return HttpResponse("<h1>Invalid Details</h1>")
    return render(request,'MyApp1/EmpForm.html',{'form':form})

