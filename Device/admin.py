from django.contrib import admin
from .models import Device, DeviceCategory, Vender, Part, Project


# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['parts', 'name']

admin.site.register(DeviceCategory)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Vender)
admin.site.register(Part)
admin.site.register(Project)
