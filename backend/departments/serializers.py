from rest_framework import serializers

from departments.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DepartmentListSerializer(serializers.ModelSerializer):
    total_employees = serializers.IntegerField()
    total_salary = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Department
        fields = "__all__"
