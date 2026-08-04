from django.db import models


# ==========================================================
# SUPPLIER MODEL
# ==========================================================

class Supplier(models.Model):

    supplier_code = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    company_name = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):

        return f"{self.supplier_code} - {self.name}"