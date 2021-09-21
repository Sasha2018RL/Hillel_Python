"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from galaxy import api_views
# Galaxy
# StarSystem
# Star
# Planet
from galaxy.api_views import GalaxyViewSet, StarSystemViewSet, StarViewSet, PlanetViewSet

router = routers.DefaultRouter()
router.register(r'Galaxy', GalaxyViewSet)
router.register(r'StarSystem', StarSystemViewSet)
router.register(r'Star', StarViewSet)
router.register(r'Planet', PlanetViewSet)

urlpatterns = [
    path("", include("car.urls")),
    path("", include("bowling.urls")),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
