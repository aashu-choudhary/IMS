from django.db import models


class Customer(models.Model):

    CUSTOMER_TYPES = [
        ("INDIVIDUAL", "Individual"),
        ("BUSINESS", "Business"),
    ]

    customer_code = models.CharField(
        max_length=20,
        unique=True,
    )

    customer_type = models.CharField(
        max_length=20,
        choices=CUSTOMER_TYPES,
        default="INDIVIDUAL",
    )

    name = models.CharField(
        max_length=200,
    )

    company_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    phone = models.CharField(
        max_length=20,
    )

    alternate_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    gst_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    pan_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100,
    )

    state = models.CharField(
        max_length=100,
    )

    country = models.CharField(
        max_length=100,
        default="India",
    )

    postal_code = models.CharField(
        max_length=15,
    )

    credit_limit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    opening_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    outstanding_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f"{self.customer_code} - {self.name}"