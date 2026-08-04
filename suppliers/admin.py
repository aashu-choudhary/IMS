from django.contrib import admin

from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = (

        "supplier_code",

        "name",

        "company_name",

        "phone",

        "is_active",

    )

    search_fields = (

        "supplier_code",

        "name",

        "company_name",

    )