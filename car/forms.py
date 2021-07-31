from django import forms
from car.models import Car, Company


class CarForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    # vin_number = forms.CharField(max_length=100)

    class Meta:
        model = Car
        fields = "__all__"


class CompanyForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    # vin_number = forms.CharField(max_length=100)

    class Meta:
        model = Company
        fields = "__all__"
