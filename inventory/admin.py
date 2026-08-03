from django.contrib import admin

from .models import (
    Brand,
    Category,
    Product,
    Stock,
    StockMovement,
    Unit,
    Warehouse,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
    )


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "short_name",
        "is_active",
    )

    search_fields = (
        "name",
        "short_name",
    )


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "city",
        "is_active",
    )

    list_filter = (
        "city",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "sku",
        "name",
        "category",
        "brand",
        "selling_price",
        "is_active",
    )

    list_filter = (
        "category",
        "brand",
        "is_active",
    )

    search_fields = (
        "sku",
        "name",
        "barcode",
    )


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "warehouse",
        "quantity",
        "available_quantity",
        "last_updated",
    )

    list_filter = (
        "warehouse",
    )

    search_fields = (
        "product__name",
        "warehouse__name",
    )


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):

    list_display = (
        "stock",
        "movement_type",
        "quantity",
        "created_by",
        "created_at",
    )

    list_filter = (
        "movement_type",
        "created_at",
    )

    search_fields = (
        "stock__product__name",
        "reference_number",
    )

    ordering = (
        "-created_at",
    )