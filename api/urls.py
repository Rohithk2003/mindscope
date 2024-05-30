from django.urls import path, include
from . import views

urlpatterns = [
    path("updateDB", views.updateDB, name="updateDB"),
    path("login", views.login, name="login"),
    path("deleteAll", views.deleteAll, name="deleteAll"),
    path("updateTimer", views.updateTimer, name="updatetimer"),
    path("all", views.listall, name="all"),
    path("pastTests", views.getPastTests, name="pastTests"),
]
