from django.db import models

from departments.models import Department


class EmployerName(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Position(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.OneToOneField(EmployerName, on_delete=models.PROTECT)
    photo = models.ImageField(blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT, related_name="employers")
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveSmallIntegerField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="employers")
    manager = models.OneToOneField("Employee", on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name.first_name} {self.full_name.last_name}: {self.position}"

