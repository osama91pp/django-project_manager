from django.contrib import admin
from . import models
from django.utils.translation import gettext as _
from django.db.models import Count

# Register your models here.
admin.site.register(models.Category)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'category', 'created_at', 'task_count')
    list_per_page = 10
    list_select_related = ('user', 'category')
    list_editable = ('status',)

    def task_count(self, obj):
        return obj.task_count

    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query. annotate (task_count=Count('task'))
        return query


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'project', 'is_completed')
    list_per_page = 10
    list_editable = ['is_completed']


admin.site.site_header = _("Projects Management")
admin.site.site_title = _("Projects Management")
# admin.site.index_title = _("Projects Management")