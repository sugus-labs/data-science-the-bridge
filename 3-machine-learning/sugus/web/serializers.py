from django.contrib.auth.models import User, Group
from rest_framework import serializers
from web.models import Name

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Name
        fields = ['text', 'prob_f', 'prob_m', 'gender']
        lookup_field = 'text'
        extra_kwargs = {
            'url': {'lookup_field': 'text'}
        }      