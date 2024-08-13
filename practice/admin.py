from django.contrib import admin
from .models import Student

# Register your models here.
@admin.action(description="Mark selected stories as published")
def make_status(modeladmin, request, queryset):
    queryset.update(status="m")
class StudentAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'status', 'is_sportsman', 'is_speaker']
    list_filter = ["name"]
    search_fields = ["name", "email"]
    actions=[make_status]

admin.site.register(Student,StudentAdmin)
