from django.contrib import admin

from .models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('key', 'uuid', 'user', 'title', 'tags', 'file_loc')

admin.site.register(File, FileAdmin)
