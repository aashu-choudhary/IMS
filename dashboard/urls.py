from django import views
from django.urls import path
from .views import dashboard_view, reports
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path(

    "reports/",

    views.reports,

    name="reports",

),
]