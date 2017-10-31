# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Nursery, Param, Sample
from .serializers import NurserySerializer, ParamSerializer, SampleSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class NurseryView(viewsets.ModelViewSet):
    queryset = Nursery.objects.all()
    serializer_class = NurserySerializer


class ParamView(viewsets.ModelViewSet):
    queryset = Param.objects.all()
    serializer_class = ParamSerializer


class SampleView(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nursery',)

 #   def get_queryset(self):

  #      nursery = self.request.query_params.get('nursery', None)
   #     print nursery
    #    if nursery is not None:
     #       queryset = queryset.filter(nursery_id=int(nursery))
      #  return queryset


class CreateSamplesView(viewsets.ViewSet):
    def create(self, request):
        print request
