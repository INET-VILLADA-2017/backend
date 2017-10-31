from django.contrib.auth.models import User, Group
from .models import Nursery, Param, Sample
from rest_framework import serializers


class NurserySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nursery
        fields = '__all__'


class ParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Param
        fields = '__all__'


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    param = ParamSerializer()
    nursery = NurserySerializer()

    class Meta:
        model = Sample
        fields = ('date', 'value', 'unit', 'state_transducer', 'duration', 'state_transmission', 'nursery', 'param')
        extra_kwargs = {
            'url': {'view_name': 'sample-detail', 'lookup_field': 'url'},
        }
