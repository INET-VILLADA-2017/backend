#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
#router.register(r'deleteTemperature', DeleteTemperatureView, base_name="deleteTemperature")
urlpatterns = [
               url(r'^api/', include(router.urls, namespace='api')),
               ]