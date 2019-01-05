from django.contrib import admin
from .models import *

admin.site.site_header = "Language Settings Admin"
admin.site.site_title = "Language App Admin Portal"
admin.site.index_title = "Welcome to Language App Portal"


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """ Admin class for Sentup Subject Result."""

    list_display = (
        "__str__", "created",
    )

admin.site.register(Lesson)


from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

admin.site.unregister(Group)
admin.site.unregister(Site)
