from django.urls import path
from bowling.views import RowListView, RowSessionDetailView, RowSessionCreateView, RowCreateView, RowDetailView, \
    RowSessionListView, PlayerCreateView, PlayerDetailView, PlayerListView

urlpatterns = [
    path("row/", RowListView.as_view(), name="row-list"),
    path("row/<int:pk>", RowDetailView.as_view(), name="row-detail"),
    path("row/create", RowCreateView.as_view(), name="row-create"),
    path(
        "row_session/create",
        RowSessionCreateView.as_view(),
        name="row_session-create"
    ),
    path("row_session/<int:pk>",
         RowSessionDetailView.as_view(),
         name="row_session-detail"
         ),
    path("row_session/", RowSessionListView.as_view(), name="row_session-list"),
    path("player/<int:pk>", PlayerDetailView.as_view(), name='player-detail'),
    path("player/create", PlayerCreateView.as_view(), name='player-create'),
    path("player/", PlayerListView.as_view(), name="row_session-list")
    # path("car/<int:pk>", CarDetailView.as_view(), name="car-detail" ),
]
