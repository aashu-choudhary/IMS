from . import views
from django.urls import path
from django.shortcuts import get_object_or_404
from .models import Brand
from .forms import BrandForm
from .views import (
    inventory_dashboard,
    category_list,
    category_create,
    category_update,
    category_delete,
    product_create,
    product_list,
)


app_name = "inventory"


urlpatterns = [

    # ======================================================
    # Inventory Dashboard
    # ======================================================

    path(
        "",
        inventory_dashboard,
        name="dashboard",
    ),


    # ======================================================
    # Category
    # ======================================================

    path(
        "categories/",
        category_list,
        name="category_list",
    ),
 
    path(
        "categories/<int:pk>/edit/",
        category_update,
        name="category_update",
    ),

    path(
        "categories/<int:pk>/delete/",
        category_delete,
        name="category_delete",
    ),
    path(
    "products/",
    product_list,
    name="product_list",
     ),

    path(
        "products/add/",
        product_create,
        name="product_create",
    ),
    path(

    "categories/add/",

    views.category_create,

    name="category_create",

    ),
    
    
    path(

    "brands/",

    views.brand_list,

    name="brand_list",

    ),
    path(

    "brands/add/",

    views.brand_create,

    name="brand_create",

    ),
    path(
    "brands/<int:pk>/edit/",
    views.brand_update,
    name="brand_update",
),
path(

    "units/<int:pk>/edit/",

    views.unit_update,

    name="unit_update",

),

path(

    "units/<int:pk>/delete/",

    views.unit_delete,

    name="unit_delete",

),    
path(

    "warehouses/<int:pk>/edit/",

    views.warehouse_update,

    name="warehouse_update",

),

path(

    "warehouses/<int:pk>/delete/",

    views.warehouse_delete,

    name="warehouse_delete",

),
path(
    "brands/<int:pk>/delete/",
    views.brand_delete,
    name="brand_delete",
),
    path(

    "units/add/",

    views.unit_create,

    name="unit_create",

    ),
     path(

    "units/",

    views.unit_list,

    name="unit_list",

     ), 
    path(

    "warehouses/",

    views.warehouse_list,

    name="warehouse_list",

    ), 
    path(

    "warehouses/add/",

    views.warehouse_create,

    name="warehouse_create",

    ),
    path(

    "stock/",

    views.stock_list,

    name="stock_list",

),
    path(

    "stock/<int:pk>/edit/",

    views.stock_update,

    name="stock_update",

),

path(

    "stock/<int:pk>/delete/",

    views.stock_delete,

    name="stock_delete",

),
path(

    "stock-movements/<int:pk>/edit/",

    views.stock_movement_update,

    name="stock_movement_update",

),

path(

    "stock-movements/<int:pk>/delete/",

    views.stock_movement_delete,

    name="stock_movement_delete",

),
path(

    "stock/<int:pk>/edit/",

    views.stock_update,

    name="stock_update",

),

path(

    "stock/<int:pk>/delete/",

    views.stock_delete,

    name="stock_delete",

),
    path(

    "stock/add/",

    views.stock_create,

    name="stock_create",

),
    path(

    "stock-movements/",

    views.stock_movement_list,

    name="stock_movement_list",

),
    path(

    "stock-movements/add/",

    views.stock_movement_create,

    name="stock_movement_create",

),
    path(

    "products/<int:pk>/edit/",

    views.product_update,

    name="product_update",

),

path(

    "products/<int:pk>/delete/",

    views.product_delete,

    name="product_delete",

),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
]