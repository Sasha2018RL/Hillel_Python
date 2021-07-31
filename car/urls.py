from django.urls import path, include
from car.views import CarListView, CarDetailView, CarCreateView, CompanyListView, CompanyDetailView, CompanyCreateView

urlpatterns = [
    path("car/", CarListView.as_view(), name="car-list"),
    path("company/", CompanyListView.as_view(), name="company-list"),
    path("company/<int:pk>", CompanyDetailView.as_view(), name="company-detail"),
    path("car/create", CarCreateView.as_view(), name="car-create"),
    path("company/create", CompanyCreateView.as_view(), name="company-create"),
    path("car/<int:pk>", CarDetailView.as_view(), name="car-detail"),
    # path("car/companies")
]
