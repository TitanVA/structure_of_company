from rest_framework import serializers

from departments.serializers import DepartmentSerializer
from employees.models import Employee, EmployerName, Position


class EmployerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerName
        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    full_name = EmployerNameSerializer()
    position = PositionSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = "__all__"
