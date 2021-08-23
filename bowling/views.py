from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from bowling.models import Row, RowSession, Player
from bowling.forms import RowSessionCreateForm, RowCreateForm, PlayerCreateForm


# Create your views here.
class RowListView(ListView):
    template_name = "row_list.html"

    model = Row

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of row",
        })
        print(dict(context))
        return context


class RowSessionListView(ListView):
    template_name = "row_session_list.html"

    model = RowSession

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of row sessions",
        })
        print(dict(context))
        return context


class RowSessionDetailView(DetailView):
    template_name = "row_session_detail.html"

    model = RowSession

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class RowDetailView(DetailView):
    template_name = "row_detail.html"

    model = Row

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # sessions = context['row'].row_sessions.all()#.select_related()  # .filter(id=context['row'].id)
        context.update({
            "row_sessions": context['row'].row_sessions.all()
        })
        return context


class RowSessionCreateView(CreateView):
    template_name = "row_session_create.html"

    model = Row
    form_class = RowSessionCreateForm


class RowCreateView(CreateView):
    template_name = "row_create.html"

    model = Row
    form_class = RowCreateForm


class PlayerCreateView(CreateView):
    template_name = "player_create.html"

    model = Player
    form_class = PlayerCreateForm


class PlayerDetailView(DetailView):
    template_name = "player_detail.html"

    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PlayerListView(ListView):
    template_name = "player_list.html"

    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(dir(context['page_obj']))
        return context
