from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('done', 'name', 'published', 'done_time')
    list_display_links = ('name',)


admin.site.register(Task, TaskAdmin)
