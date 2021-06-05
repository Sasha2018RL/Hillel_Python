from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    vin_number = models.CharField(max_length=100)
    car_model = models.ForeignKey("car.CarModel", on_delete=models.SET_NULL, null=True)

    def company(self):
        return self.car_model.company

    def __str__(self):
        return f"Name:{self.name} vin_number: {self.vin_number}"

class CarModel(models.Model):

    name = models.CharField(max_length=100)
    company = models.ForeignKey("car.Company", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Company(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"
