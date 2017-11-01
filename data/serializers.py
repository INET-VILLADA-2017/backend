from django.contrib.auth.models import User, Group
from .models import Nursery, Param, Sample, Config
from rest_framework import serializers
from rest_auth.models import TokenModel
import requests

class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = TokenModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("is_staff", 'is_superuser')


class NurserySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nursery
        fields = '__all__'


class ParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Param
        fields = '__all__'


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.spray_volume = validated_data.get('spray_volume', instance.spray_volume)
        instance.degree_of_shadow = validated_data.get('degree_of_shadow', instance.degree_of_shadow)
        instance.watering_period_1 = validated_data.get('watering_period_1', instance.watering_period_1)
        instance.watering_period_2 = validated_data.get('watering_period_2', instance.watering_period_2)
        instance.watering_period_2 = validated_data.get('watering_period_2', instance.watering_period_2)
        r = requests.post('http://168.83.20.187/?vr={spray}&so={degree}&pr1={w1}&pr2={w2}'.format(
                spray=instance.spray_volume,
                degree=instance.degree_of_shadow,
                w1=instance.watering_period_1,
                w2=instance.watering_period_2
        ), data={})
        print r
        return instance
    # ?vr = 10 & so = 10 & pr1 = 10 & pr2 = 10


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    param = ParamSerializer()
    nursery = NurserySerializer()

    class Meta:
        model = Sample
        fields = ('date', 'value', 'unit', 'state_transducer', 'duration', 'state_transmission', 'nursery', 'param')
        extra_kwargs = {
            'url': {'view_name': 'sample-detail', 'lookup_field': 'url'},
        }
