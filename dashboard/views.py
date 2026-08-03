from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from customers.models import Customer
from django.db.models import F
from inventory.models import (
    Product,
    Stock,
    StockMovement,
)

# ==========================================================
# MAIN DASHBOARD
# ==========================================================

@login_required(login_url="login")
def dashboard_view(request):

    # ======================================================
    # DASHBOARD CARDS
    # ======================================================

    total_products = Product.objects.count()

    total_customers = Customer.objects.count()

    low_stock_products = (
        Stock.objects.filter(
            available_quantity__lte=F("minimum_stock")
        )
        .select_related(
            "product",
            "product__category",
            "warehouse",
        )
        .order_by("available_quantity")
    )

    low_stock_count = low_stock_products.count()

    # Sales module not built yet
    today_invoices = 0

    # ==========================================
    # Recent Activities
    # ==========================================

    recent_movements = (
        StockMovement.objects.select_related(
            "stock__product",
            "created_by",
        )
        .order_by("-created_at")[:8]
    )

    recent_activities = []

    for movement in recent_movements:

        if movement.movement_type == "IN":
            icon = "fa-solid fa-arrow-down"

        elif movement.movement_type == "OUT":
            icon = "fa-solid fa-arrow-up"

        elif movement.movement_type == "TRANSFER":
            icon = "fa-solid fa-right-left"

        else:
            icon = "fa-solid fa-pen"

        recent_activities.append({

            "icon": icon,

            "title": movement.stock.product.name,

            "description": (
                f"{movement.movement_type} "
                f"({movement.quantity}) "
                f"by {movement.created_by.username}"
            ),

            "created_at": movement.created_at.strftime(
                "%d %b %Y %I:%M %p"
            ),

        })

    # ==========================================
    # Context
    # ==========================================

    context = {

        # Dashboard Cards
        "total_products": total_products,

        "low_stock_count": low_stock_count,

        "total_customers": total_customers,

        "today_invoices": today_invoices,

        # Dashboard Sections
        "low_stock_products": low_stock_products,

        "recent_activities": recent_activities,

    }

    return render(

        request,

        "admin/dashboard.html",

        context,

    )
# ==========================================================
# REPORTS DASHBOARD
# ==========================================================

@login_required(login_url="login")
def reports(request):

    return render(

        request,

        "dashboard/reports.html",

    )    
# ======================================================
# RECENT ACTIVITIES
# ======================================================

recent_movements = (
    StockMovement.objects
    .select_related(
        "stock__product",
        "created_by",
    )
    .order_by("-created_at")[:8]
)

recent_activities = []

for movement in recent_movements:

    if movement.movement_type == "IN":

        title = "Stock Added"
        icon = "fa-solid fa-circle-arrow-down"

    elif movement.movement_type == "OUT":

        title = "Stock Removed"
        icon = "fa-solid fa-circle-arrow-up"

    elif movement.movement_type == "TRANSFER":

        title = "Stock Transfer"
        icon = "fa-solid fa-right-left"

    else:

        title = "Stock Adjustment"
        icon = "fa-solid fa-pen"

    recent_activities.append({

        "icon": icon,

        "title": title,

        "description": (
            f"{movement.quantity} Units of "
            f"{movement.stock.product.name}"
        ),

        "user": movement.created_by.username,

        "created_at": movement.created_at.strftime(
            "%d %b %Y • %I:%M %p"
        ),

    })    