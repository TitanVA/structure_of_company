from django.db import models

from departments.models import Department


class EmployerName(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)


class Position(models.Model):
    name = models.CharField(max_length=30)


class Employee(models.Model):
    full_name = models.OneToOneField(EmployerName, on_delete=models.PROTECT)
    photo = models.ImageField()
    position = models.ForeignKey(Position, on_delete=models.PROTECT, related_name="employers")
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveSmallIntegerField()
    department = models.OneToOneField(Department, on_delete=models.PROTECT)

