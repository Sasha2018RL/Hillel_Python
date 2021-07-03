from django.urls import path
from bowling.views import RowListView, RowSessionDetailView, RowSessionCreateView
urlpatterns = [
    path("row/", RowListView.as_view(), name="row-list" ),
    path(
        "row_session/create",
        RowSessionCreateView.as_view(),
        name="row_session-create"
    ),
    path("row_session/<int:pk>",
        RowSessionDetailView.as_view(),
        name="row_session-detail"
    ),
    # path("car/<int:pk>", CarDetailView.as_view(), name="car-detail" ),
]
