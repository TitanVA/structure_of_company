from django.db import models

from employees.models import Employee


class Project(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="projects")
    employees = models.ManyToManyField(Employee, related_name="employee_project")

    def __str__(self):
        return self.name
