from django.contrib.auth.models import User, Group
from .models import Nursery, Param, Sample
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
