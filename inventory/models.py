from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["name"]

        verbose_name = "Category"

        verbose_name_plural = "Categories"

    def __str__(self):

        return self.name
class Brand(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["name"]

        verbose_name = "Brand"

        verbose_name_plural = "Brands"

    def __str__(self):

        return self.name

class Unit(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True
    )

    short_name = models.CharField(
        max_length=20,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["name"]

        verbose_name = "Unit"

        verbose_name_plural = "Units"

    def __str__(self):

        return f"{self.name} ({self.short_name})"   
     
class Product(models.Model):

    sku = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(
        max_length=200
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name="products"
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.PROTECT,
        related_name="products"
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )
    purchase_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00
    )

    selling_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00
    )

    barcode = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["name"]

        verbose_name = "Product"

        verbose_name_plural = "Products"

    def __str__(self):

        return f"{self.sku} - {self.name}"         
class Warehouse(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True
    )

    code = models.CharField(
        max_length=20,
        unique=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    state = models.CharField(
        max_length=100,
        blank=True
    )

    country = models.CharField(
        max_length=100,
        default="India"
    )

    contact_person = models.CharField(
        max_length=100,
        blank=True
    )

    contact_number = models.CharField(
        max_length=20,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ["name"]

        verbose_name = "Warehouse"

        verbose_name_plural = "Warehouses"

    def __str__(self):

        return self.name  

class Stock(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="stocks"
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="stocks"
    )

    quantity = models.PositiveIntegerField(
        default=0
    )

    reserved_quantity = models.PositiveIntegerField(
        default=0
    )

    available_quantity = models.PositiveIntegerField(
        default=0
    )

    minimum_stock = models.PositiveIntegerField(
        default=0
    )

    maximum_stock = models.PositiveIntegerField(
        default=0
    )

    reorder_level = models.PositiveIntegerField(
        default=0
    )

    last_updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        unique_together = ("product", "warehouse")

        ordering = ["product__name"]

        verbose_name = "Stock"

        verbose_name_plural = "Stock"

    def __str__(self):

        return f"{self.product.name} - {self.warehouse.name}"
 
class StockMovement(models.Model):

    MOVEMENT_TYPES = [

        ("IN", "Stock In"),

        ("OUT", "Stock Out"),

        ("TRANSFER", "Transfer"),

        ("ADJUSTMENT", "Adjustment"),

    ]


    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name="movements"
    )

    movement_type = models.CharField(
        max_length=20,
        choices=MOVEMENT_TYPES
    )

    quantity = models.PositiveIntegerField()

    reference_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        "auth.User",
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["-created_at"]

        verbose_name = "Stock Movement"

        verbose_name_plural = "Stock Movements"

    def __str__(self):

        return f"{self.stock.product.name} - {self.movement_type}"            