from django.contrib import admin

# Register your models here.
from .models import jobs


class JobsAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')


admin.site.register(jobs, JobsAdmin)