# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Nursery, Param, Sample
from .serializers import NurserySerializer, ParamSerializer, SampleSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class NurseryView(viewsets.ModelViewSet):
    """
        /param
        Get all nurseries
    """
    queryset = Nursery.objects.all()
    serializer_class = NurserySerializer


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


class CreateSamplesView(viewsets.ViewSet):
    def create(self, request):
        print request
        param = Param.objects.all().filter(param_id=id)


        print request
