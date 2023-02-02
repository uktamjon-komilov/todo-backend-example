from django.urls import path

from .views import ToDoListView

urlpatterns = [
    path("", ToDoListView.as_view(), name="list-todos"),
]