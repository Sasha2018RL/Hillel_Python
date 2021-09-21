from rest_framework import viewsets

from galaxy.models import Galaxy, Planet, Star, StarSystem
from galaxy.serializer import GalaxySerializer, PlanetSerializer, StarSerializer, StarSystemSerializer


class GalaxyViewSet(viewsets.ModelViewSet):
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer


class StarSystemViewSet(viewsets.ModelViewSet):
    queryset = StarSystem.objects.all()
    serializer_class = StarSystemSerializer


class StarViewSet(viewsets.ModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
