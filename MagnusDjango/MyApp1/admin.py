from django.contrib import admin
from .models import Employee,Dept,Car
# Register your models here.

admin.site.register(Employee)
admin.site.register(Dept)
admin.site.register(Car)