from django.db.models import Count, Sum
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from departments.models import Department
from departments.serializers import DepartmentSerializer, DepartmentListSerializer


class DepartmentViewSet(ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']

    def get_queryset(self):
        if self.action == "list":
            return Department.objects.all().annotate(
                total_employees=Count("employers")).annotate(
                total_salary=Sum("employers__rate"))
        return Department.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return DepartmentListSerializer
        return DepartmentSerializer
