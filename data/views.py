# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Nursery, Param, Sample, Config
from .serializers import NurserySerializer, ParamSerializer, SampleSerializer, UserSerializer, ConfigSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class NurseryView(viewsets.ModelViewSet):
    """
        /nursery
        Get all nurseries
    """
    queryset = Nursery.objects.all()
    serializer_class = NurserySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ConfigView(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


class ParamView(viewsets.ModelViewSet):
    """
        /param
        Get all parameters
    """
    queryset = Param.objects.all()
    serializer_class = ParamSerializer


class SampleView(viewsets.ModelViewSet):
    """
        /sample
        Get all samples and you can filter for nursery usin ?nursery=ID
    """
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nursery',)
