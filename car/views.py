from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from car.models import Car, Company
from car.forms import CarForm, CompanyForm
from django.views.generic.edit import CreateView


# Create your views here.

class CarListView(ListView):
    template_name = "car_list.html"

    model = Car
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of car",
            "list_len": len(context["car_list"])
        })
        return context


class CompanyListView(ListView):
    template_name = "company_list.html"

    model = Company
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of companies",
            "list_len": len(context["company_list"])
        })
        return context


class CarDetailView(DetailView):
    """docstring for CarDetailView."""
    template_name = "car.html"
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CompanyDetailView(DetailView):
    """docstring for CompanyDetailView."""
    template_name = "company.html"
    model = Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CarCreateView(CreateView):
    template_name = "car_create.html"

    model = Car
    form_class = CarForm


class CompanyCreateView(CreateView):
    template_name = "company_create.html"

    model = Company
    form_class = CompanyForm

# def car_create(request):
#     if request.method == "POST":
#         form = CarForm(request.POST)
#         print("post")
#         if form.is_valid():
#             form.save()
#             return redirect("car-detail", pk=form.instance.pk)
#     form = CarForm()
#     return render(request,"car_create.html",{"form":form})

# def car_view(request, obj=None):
#     car = get_object_or_404(Car,pk=obj)
#     context= {
#         "car":car
#     }
#     return render(request,"car.html", context)
