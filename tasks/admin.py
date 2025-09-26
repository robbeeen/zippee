from django.contrib import admin

# Register your models here.
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('completed', 'created_at', 'updated_at')
    ordering = ('-created_at',)