from django.contrib import admin
from . import models
from django.utils.translation import gettext as _

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Project)
admin.site.register(models.Task)

admin.site.site_header = _("Projects Management")
admin.site.site_title = _("Projects Management")
# admin.site.index_title = _("Projects Management")