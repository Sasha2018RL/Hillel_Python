from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from bowling.models import Row
from bowling.forms import RowSessionCreateForm
# Create your views here.
class RowListView(ListView):

    template_name = "row_list.html"

    model = Row
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"List of row",
            })
        print(dict(context))
        return context

class RowSessionDetailView(DetailView):

    template_name = "row_session_detail.html"

    model = Row

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RowSessionCreateView(CreateView):

    template_name = "row_session_create.html"

    model = Row
    form_class = RowSessionCreateForm


    def get(self, request, *args, **kwargs):
        data = request.GET
        user = User.objects.get(pk=request.session["_auth_user_id"])
        if data:
            row = Row.objects.get(pk = int(data.get("row")))
            self.initial = {"row": row,"user":user}
        return super().get(request, *args, **kwargs)
