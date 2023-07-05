from django.db.models import Count, Sum
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from departments.models import Department
from departments.serializers import DepartmentSerializer, DepartmentListSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']

    def get_serializer_class(self):
        if self.action == "list":
            return DepartmentListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        total_employees = queryset.aggregate(total_employees=Count("employers")).get("total_employees")
        total_salary = queryset.aggregate(total_salary=Sum("employers__rate")).get("total_salary")

        response_data = {"result": response.data, "total_employees": total_employees, "total_salary": total_salary}
        response.data = response_data

        return response
