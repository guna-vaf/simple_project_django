from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "roll_number",
        "first_name",
        "last_name",
        "email",
        "course",
        "age",
        "created_at",
    )
    search_fields = ("first_name", "last_name", "email", "roll_number", "course")
    list_filter = ("course", "created_at")
