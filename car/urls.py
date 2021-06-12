from django.urls import path, include
from car.views import car_view, CarListView
urlpatterns = [
    path("car/", CarListView.as_view(), name="car-list" ),
    path("car/<int:obj>", car_view ),
]
