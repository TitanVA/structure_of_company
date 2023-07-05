from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from employees.models import Employee, EmployerName, Position
from employees.serializers import EmployeeSerializer, EmployerNameSerializer, PositionSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class EmployerNameVewSet(ModelViewSet):
    queryset = EmployerName.objects.all()
    serializer_class = EmployerNameSerializer


class PositionVewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class EmployeeVewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'full_name__last_name']
    pagination_class = StandardResultsSetPagination
