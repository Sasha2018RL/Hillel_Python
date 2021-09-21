import re

from rest_framework import serializers

from galaxy.models import Galaxy, Planet, Star, StarSystem


class GalaxySerializer(serializers.ModelSerializer):
    class Meta:
        model = Galaxy

        fields = ['pk', 'name', 'size_x', 'size_y']


class StarSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarSystem

        fields = ['pk', 'name', 'galaxy', 'position_x', 'position_y']


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star

        fields = ['pk', 'name', 'color', 'star_system', 'diameter']


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet

        fields = ['pk', 'name', 'color', 'star_system', 'diameter', 'live']

