# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Nursery, Sample, Param


# Register your models here.


class NurseryAdmin(SimpleHistoryAdmin):
    list_display = ["id", "denomination", "fiscal_key", "business_name", "address"]
    search_fields = ('denomination', 'business_name', 'fiscal_key', 'address')
    history_list_display = ["status"]


class SampleAdmin(SimpleHistoryAdmin):
    list_display = ["id", "value", "state_transducer", "duration", "state_transmission", "nursery"]
    list_filter = ('date', 'unit', 'value', 'state_transducer')
    search_fields = ('value', "date", 'unit')


class ParamAdmin(SimpleHistoryAdmin):
    list_display = ["name"]


admin.site.register(Nursery, NurseryAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(Param, ParamAdmin)
