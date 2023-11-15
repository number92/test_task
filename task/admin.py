from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date',
                    'updated_date', 'scheduled_date')
    list_editable = ('name', 'scheduled_date')
