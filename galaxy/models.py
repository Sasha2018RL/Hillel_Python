from django.db import models


class CommonName(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class CommonNameColorStarSystemDiameter(CommonName):
    color = models.CharField(max_length=30)
    star_system = models.ForeignKey('galaxy.StarSystem',
                                    on_delete=models.CASCADE)

    diameter = models.PositiveIntegerField(default=1)

    class Meta:
        abstract = True


class Galaxy(CommonName):
    size_x = models.PositiveIntegerField(default=1)
    size_y = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return '/galaxy'


class StarSystem(CommonName):
    position_x = models.PositiveIntegerField(default=1)
    position_y = models.PositiveIntegerField(default=1)
    galaxy = models.ForeignKey(
        "galaxy.Galaxy",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return '/star_system'


class Star(CommonNameColorStarSystemDiameter):

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return '/star'


class Planet(CommonNameColorStarSystemDiameter):
    live = models.BooleanField(default=False)

    def get_absolute_url(self):
        return '/planet'
