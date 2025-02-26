from django.contrib import admin
from .models import *


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1


class SchoolAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]


admin.site.register(Homepage)
admin.site.register(School, SchoolAdmin)
admin.site.register(Specialization)
admin.site.register(Admin)
admin.site.register(Teacher)
admin.site.register(Gallery)
admin.site.register(Timeline)
admin.site.register(Contact)
admin.site.register(Communication)
admin.site.register(Qualification)