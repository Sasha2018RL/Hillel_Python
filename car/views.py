from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from car.models import Car
# Create your views here.

class CarListView(ListView):

    template_name = "car_list.html"

    model = Car
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(*dict(context).items(), sep="\n")
        return context



def car_view(request, obj=None):
    car = get_object_or_404(Car,pk=obj)
    context= {
        "car":car
    }
    return render(request,"car.html", context)
