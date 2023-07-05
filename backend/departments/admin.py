from django.contrib import admin

from departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
