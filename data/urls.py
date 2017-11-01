#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import NurseryView, ParamView, SampleView, UserViewSet, ConfigView

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'config', ConfigView)
router.register(r'nursery', NurseryView)
router.register(r'param', ParamView)
router.register(r'sample', SampleView, base_name='sample')
#router.register(r'createsamples', CreateSamplesView, base_name="createSamples")
urlpatterns = [
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
