from rest_framework import serializers

from employees.serializers import EmployeeSerializer
from projects.models import Project


class ProjectsListSerializer(serializers.ModelSerializer):
    employee_counter = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ("pk", "name", "employee_counter")

    def get_employee_counter(self, obj):
        return obj.employees.count()


class ProjectsDetailSerializer(serializers.ModelSerializer):
    manager = EmployeeSerializer()
    employees = EmployeeSerializer(many=True)
    employee_counter = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_employee_counter(self, obj):
        a = obj
        return a
