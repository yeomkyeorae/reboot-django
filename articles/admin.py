from django.contrib import admin

# Register your models here.
from .models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')

admin.site.register(Articles, ArticlesAdmin)