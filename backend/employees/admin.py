from django.contrib import admin
from employees.models import EmployerName, Position, Employee

admin.site.register(EmployerName)
admin.site.register(Position)
admin.site.register(Employee)
