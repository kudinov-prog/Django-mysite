from django.contrib import admin

from .models import Adb
from .models import Tag

class AdbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published', 'tag')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Adb, AdbAdmin)
admin.site.register(Tag)