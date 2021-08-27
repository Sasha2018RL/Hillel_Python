from django.contrib import admin

from galaxy.models import Galaxy, StarSystem, Star, Planet


@admin.register(Galaxy)
class GalaxyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "size_x",
        "size_y"
    ]

@admin.register(StarSystem)
class StarSystemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "position_x",
        "position_y"
    ]

@admin.register(Star)
class StarSystemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "color",
        "star_system",
        "diameter"
    ]

@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'color',
        'star_system',
        'diameter',

    ]