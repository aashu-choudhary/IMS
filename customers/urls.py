from django.urls import path
from . import views

app_name = "customers"

urlpatterns = [

    # ==========================================
    # Customer List
    # ==========================================

    path(
    "",
    views.customer_dashboard,
    name="dashboard",
),
path(

    "list/",

    views.customer_list,

    name="customer_list",

),
path(

    "create/",

    views.customer_create,

    name="customer_create",

),
path(

    "view/<int:pk>/",

    views.customer_view,

    name="customer_view",

),
path(
    "list/",
    views.customer_list,
    name="customer_list",
),

    # ==========================================
    # Customer Create
    # ==========================================

    path(
        "add/",
        views.customer_create,
        name="customer_create",
    ),

    # ==========================================
    # Customer Update
    # ==========================================

    path(
        "<int:pk>/edit/",
        views.customer_update,
        name="customer_update",
    ),

    # ==========================================
    # Customer Delete
    # ==========================================

  path(

    "delete/<int:pk>/",

    views.customer_delete,

    name="customer_delete",

),
    path(

    "edit/<int:pk>/",

    views.customer_edit,

    name="customer_edit",

),

]