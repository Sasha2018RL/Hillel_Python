from django.urls import path, include
from car.views import CarListView, CarDetailView, CarCreateView
urlpatterns = [
    path("car/", CarListView.as_view(), name="car-list" ),
    path("car/create", CarCreateView.as_view(), name="car-create" ),
    path("car/<int:pk>", CarDetailView.as_view(), name="car-detail" ),
]
