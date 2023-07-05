from rest_framework.viewsets import ModelViewSet

from employees.models import Employee, EmployerName, Position
from employees.serializers import EmployeeSerializer, EmployerNameSerializer, PositionSerializer


class EmployerNameVewSet(ModelViewSet):
    queryset = EmployerName.objects.all()
    serializer_class = EmployerNameSerializer


class PositionVewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class EmployeeVewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
