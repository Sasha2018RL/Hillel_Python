from django import forms
from bowling.models import RowSession, Row
from django.contrib.auth.models import User

class RowSessionCreateForm(forms.ModelForm):

    user = forms.ModelChoiceField(queryset=User.objects.all())
    row = forms.ModelChoiceField(queryset=Row.objects.all())
    date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    )
    # vin_number = forms.CharField(max_length=100)

    class Meta:
        model = RowSession
        fields = "__all__"
