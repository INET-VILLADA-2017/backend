# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Nursery, Device, Sample, Param, Config


# Register your models here.
class ConfigInline(admin.TabularInline):
    model = Config
    exclude = ()


class DeviceInline(admin.TabularInline):
    model = Device
    exclude = ()


class NurseryAdmin(SimpleHistoryAdmin):
    list_display = ["id", "denomination", "fiscal_key", "business_name", "address"]
    search_fields = ('denomination', 'business_name', 'fiscal_key', 'address')
    history_list_display = ["status"]


class DeviceAdmin(SimpleHistoryAdmin):
    list_display = ["id", "url", "nursery"]
    list_filter = ('nursery',)


class ConfigAdmin(SimpleHistoryAdmin):
    list_display = ["id", "spray_volume", "degree_of_shadow", "watering_period_1", "watering_period_1"]
    list_filter = ('device',)
    inline = [
        DeviceInline
    ]


class SampleAdmin(SimpleHistoryAdmin):
    list_display = ["id", "value", "state_transducer", "duration", "state_transmission", "nursery"]
    list_filter = ('date', 'unit', 'value', 'state_transducer', 'param')
    search_fields = ('value', "date", 'unit')


class ParamAdmin(SimpleHistoryAdmin):
    list_display = ["name"]


admin.site.register(Nursery, NurseryAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(Param, ParamAdmin)
