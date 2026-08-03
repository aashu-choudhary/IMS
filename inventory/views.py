# ==========================================================
# INVENTORY VIEWS
# ==========================================================

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db.models import Q
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from .forms import (
    CategoryForm,
    BrandForm,
    UnitForm,
    WarehouseForm,
    ProductForm,
    StockForm,
    StockMovementForm,
)

from .forms import BrandForm
from .forms import CategoryForm

from .models import (
    Category,
    Product,
    Brand,
    Unit,
    Warehouse,
    Stock,
    StockMovement,
)


# ==========================================================
# INVENTORY DASHBOARD
# ==========================================================

@login_required(login_url="login")
def inventory_dashboard(request):

    total_products = Product.objects.count()

    total_categories = Category.objects.count()

    total_warehouses = Warehouse.objects.count()

    recent_products = Product.objects.select_related(

        "category",

        "brand",

        "unit",

    ).order_by(

        "-created_at"

    )[:5]

    low_stock_products = Stock.objects.select_related(

        "product",

        "warehouse",

    ).filter(

        available_quantity__lte=F(

            "reorder_level"

        )

    ).order_by(

        "available_quantity"

    )[:5]

    context = {

        "total_products": total_products,

        "total_categories": total_categories,

        "total_warehouses": total_warehouses,

        "low_stock_count": low_stock_products.count(),

        "recent_products": recent_products,

        "low_stock_products": low_stock_products,

    }

    return render(

        request,

        "inventory/dashboard.html",

        context,

    )




# ==========================================================
# PRODUCT LIST
# ==========================================================

@login_required(login_url="login")
def product_list(request):
    search = request.GET.get("search", "").strip()
    category = request.GET.get("category", "")
    brand = request.GET.get("brand", "")
    warehouse = request.GET.get("warehouse", "")
    status = request.GET.get("status", "")

    products = Product.objects.select_related(
        "category",
        "brand",
        "unit",
    ).prefetch_related(
        "stocks",
    )

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(sku__icontains=search) |
            Q(barcode__icontains=search) |
            Q(description__icontains=search)
        )

    if category:
        products = products.filter(category_id=category)

    if brand:
        products = products.filter(brand_id=brand)

    if warehouse:
        products = products.filter(
            stocks__warehouse_id=warehouse
        )

    if status == "active":
        products = products.filter(is_active=True)

    elif status == "inactive":
        products = products.filter(is_active=False)

    context = {
        "products": products.distinct().order_by("name"),

        "categories": Category.objects.order_by("name"),
        "brands": Brand.objects.order_by("name"),
        "warehouses": Warehouse.objects.order_by("name"),

        "search": search,
        "selected_category": category,
        "selected_brand": brand,
        "selected_warehouse": warehouse,
        "selected_status": status,
    }

    return render(
        request,
        "inventory/product_list.html",
        context,
    )
# ==========================================================
# CATEGORY LIST
# ==========================================================

@login_required(login_url="login")
def category_list(request):

    search = request.GET.get(

        "search",

        ""

    )

    categories = Category.objects.all()

    if search:

        categories = categories.filter(

            name__icontains=search

        )

    context = {

        "categories": categories.order_by(

            "name"

        ),

        "search": search,

    }

    return render(

        request,

        "inventory/category_list.html",

        context,

    )
    # ==========================================================
# CATEGORY CREATE
# ==========================================================

@login_required(login_url="login")
def category_create(request):

    if request.method == "POST":

        form = CategoryForm(

            request.POST

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Category created successfully."

            )

            return redirect(

                "inventory:category_list"

            )

    else:

        form = CategoryForm()

    context = {

        "form": form,

        "title": "Add Category",

    }

    return render(

        request,

        "inventory/category_form.html",

        context,

    )


# ==========================================================
# CATEGORY UPDATE
# ==========================================================

@login_required(login_url="login")
def category_update(request, pk):

    category = get_object_or_404(

        Category,

        pk=pk,

    )

    if request.method == "POST":

        form = CategoryForm(

            request.POST,

            instance=category,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Category updated successfully."

            )

            return redirect(

                "inventory:category_list"

            )

    else:

        form = CategoryForm(

            instance=category,

        )

    context = {

        "form": form,

        "title": "Edit Category",

    }

    return render(

        request,

        "inventory/category_form.html",

        context,

    )


# ==========================================================
# CATEGORY DELETE
# ==========================================================

@login_required(login_url="login")
def category_delete(request, pk):

    category = get_object_or_404(

        Category,

        pk=pk,

    )

    if request.method == "POST":

        category.delete()

        messages.success(

            request,

            "Category deleted successfully."

        )

        return redirect(

            "inventory:category_list"

        )

    context = {

        "category": category,

    }

    return render(

        request,

        "inventory/category_delete.html",

        context,

    )
    
# ==========================================================
# BRAND LIST
# ==========================================================

@login_required(login_url="login")
def brand_list(request):

    search = request.GET.get(

        "search",

        ""

    )

    brands = Brand.objects.all()

    if search:

        brands = brands.filter(

            name__icontains=search

        )

    context = {

        "brands": brands,

        "search": search,

    }

    return render(

        request,

        "inventory/brand_list.html",

        context,

    )

    brands = Brand.objects.all().order_by(

        "name"

    )

    context = {

        "brands": brands,

    }

    return render(

        request,

        "inventory/brand_list.html",

        context,

    )  
# ==========================================================
# BRAND CREATE
# ==========================================================

@login_required(login_url="login")
def brand_create(request):

    if request.method == "POST":

        form = BrandForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Brand created successfully."

            )

            return redirect(

                "inventory:brand_list"

            )

    else:

        form = BrandForm()

    context = {

        "form": form,

    }

    return render(

        request,

        "inventory/brand_form.html",

        context,

    )
@login_required(login_url="login")
def brand_update(request, pk):

    brand = get_object_or_404(

        Brand,

        pk=pk

    )

    if request.method == "POST":

        form = BrandForm(

            request.POST,

            instance=brand

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Brand updated successfully."

            )

            return redirect(

                "inventory:brand_list"

            )

    else:

        form = BrandForm(

            instance=brand

        )

    return render(

        request,

        "inventory/brand_form.html",

        {

            "form": form,

        },

    )


@login_required(login_url="login")
def brand_delete(request, pk):

    brand = get_object_or_404(

        Brand,

        pk=pk

    )

    if request.method == "POST":

        brand.delete()

        messages.success(

            request,

            "Brand deleted successfully."

        )

    return redirect(

        "inventory:brand_list"

    )    
# ==========================================================
# UNIT LIST
# ==========================================================

@login_required(login_url="login")
def unit_list(request):

    search = request.GET.get(

        "search",

        ""

    )

    units = Unit.objects.all()

    if search:

        units = units.filter(

            name__icontains=search

        )

    context = {

        "units": units.order_by(

            "name"

        ),

        "search": search,

    }

    return render(

        request,

        "inventory/unit_list.html",

        context,

    )

    return render(

        request,

        "inventory/unit_list.html",

    )
# ==========================================================
# UNIT CREATE
# ==========================================================

@login_required(login_url="login")
def unit_create(request):

    if request.method == "POST":

        form = UnitForm(

            request.POST

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Unit created successfully."

            )

            return redirect(

                "inventory:unit_list"

            )

    else:

        form = UnitForm()

    context = {

        "form": form,

        "title": "Add Unit",

    }

    return render(

        request,

        "inventory/unit_form.html",

        context,

    )

    return render(

        request,

        "inventory/unit_form.html",

    )
# ==========================================================
# UNIT UPDATE
# ==========================================================

@login_required(login_url="login")
def unit_update(request, pk):

    unit = get_object_or_404(

        Unit,

        pk=pk,

    )

    if request.method == "POST":

        form = UnitForm(

            request.POST,

            instance=unit,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Unit updated successfully."

            )

            return redirect(

                "inventory:unit_list"

            )

    else:

        form = UnitForm(

            instance=unit,

        )

    context = {

        "form": form,

        "title": "Edit Unit",

    }

    return render(

        request,

        "inventory/unit_form.html",

        context,

    )
# ==========================================================
# UNIT DELETE
# ==========================================================

@login_required(login_url="login")
def unit_delete(request, pk):

    unit = get_object_or_404(

        Unit,

        pk=pk,

    )

    if request.method == "POST":

        unit.delete()

        messages.success(

            request,

            "Unit deleted successfully."

        )

    return redirect(

        "inventory:unit_list"

    )        
# ==========================================================
# WAREHOUSE LIST
# ==========================================================

# ==========================================================
# WAREHOUSE LIST
# ==========================================================

@login_required(login_url="login")
def warehouse_list(request):

    search = request.GET.get(

        "search",

        ""

    )

    warehouses = Warehouse.objects.all()

    if search:

        warehouses = warehouses.filter(

            name__icontains=search

        )

    context = {

        "warehouses": warehouses.order_by(

            "name"

        ),

        "search": search,

    }

    return render(

        request,

        "inventory/warehouse_list.html",

        context,

    )

    return render(

        request,

        "inventory/warehouse_list.html",

    )
# ==========================================================
# WAREHOUSE CREATE
# ==========================================================

# ==========================================================
# WAREHOUSE CREATE
# ==========================================================

@login_required(login_url="login")
def warehouse_create(request):

    if request.method == "POST":

        form = WarehouseForm(

            request.POST

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Warehouse created successfully."

            )

            return redirect(

                "inventory:warehouse_list"

            )

    else:

        form = WarehouseForm()

    context = {

        "form": form,

        "title": "Add Warehouse",

    }

    return render(

        request,

        "inventory/warehouse_form.html",

        context,

    )

    return render(

        request,

        "inventory/warehouse_form.html",

    )
# ==========================================================
# WAREHOUSE UPDATE
# ==========================================================

@login_required(login_url="login")
def warehouse_update(request, pk):

    warehouse = get_object_or_404(

        Warehouse,

        pk=pk,

    )

    if request.method == "POST":

        form = WarehouseForm(

            request.POST,

            instance=warehouse,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Warehouse updated successfully."

            )

            return redirect(

                "inventory:warehouse_list"

            )

    else:

        form = WarehouseForm(

            instance=warehouse,

        )

    context = {

        "form": form,

        "title": "Edit Warehouse",

    }

    return render(

        request,

        "inventory/warehouse_form.html",

        context,

    )   
# ==========================================================
# WAREHOUSE DELETE
# ==========================================================

@login_required(login_url="login")
def warehouse_delete(request, pk):

    warehouse = get_object_or_404(

        Warehouse,

        pk=pk,

    )

    if request.method == "POST":

        warehouse.delete()

        messages.success(

            request,

            "Warehouse deleted successfully."

        )

    return redirect(

        "inventory:warehouse_list"

    )    
     
# ==========================================================
# STOCK LIST
# ==========================================================

@login_required(login_url="login")
def stock_list(request):

    search = request.GET.get(

        "search",

        ""

    )

    stocks = Stock.objects.select_related(

        "product",

        "warehouse",

    )

    if search:

        stocks = stocks.filter(

            product__name__icontains=search

        )

    context = {

        "stocks": stocks.order_by(

            "product__name"

        ),

        "search": search,

    }

    return render(

        request,

        "inventory/stock_list.html",

        context,

    )

    search = request.GET.get(

        "search",

        ""

    )

    stocks = Stock.objects.select_related(

        "product",

        "warehouse",

    )

    if search:

        stocks = stocks.filter(

            product__name__icontains=search

        )

    context = {

        "stocks": stocks.order_by(

            "product__name"

        ),

        "search": search,

    }

    return render(

        request,

        "inventory/stock_list.html",

        context,

    )

    return render(

        request,

        "inventory/stock_list.html",

    )
# ==========================================================
# STOCK CREATE
# ==========================================================

@login_required(login_url="login")
def stock_create(request):

    if request.method == "POST":

        form = StockForm(

            request.POST,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Stock added successfully."

            )

            return redirect(

                "inventory:stock_list"

            )

    else:

        form = StockForm()

    context = {

        "form": form,

        "title": "Add Stock",

    }

    return render(

        request,

        "inventory/stock_form.html",

        context,

    )

    if request.method == "POST":

        form = StockForm(

            request.POST,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Stock added successfully."

            )

            return redirect(

                "inventory:stock_list"

            )

    else:

        form = StockForm()

    context = {

        "form": form,

        "title": "Add Stock",

    }

    return render(

        request,

        "inventory/stock_form.html",

        context,

    )

    return render(

        request,

        "inventory/stock_form.html",

    )
# ==========================================================
# STOCK UPDATE
# ==========================================================

@login_required(login_url="login")
def stock_update(request, pk):

    stock = get_object_or_404(

        Stock,

        pk=pk,

    )

    if request.method == "POST":

        form = StockForm(

            request.POST,

            instance=stock,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Stock updated successfully."

            )

            return redirect(

                "inventory:stock_list"

            )

    else:

        form = StockForm(

            instance=stock,

        )

    context = {

        "form": form,

        "title": "Edit Stock",

    }

    return render(

        request,

        "inventory/stock_form.html",

        context,

    )

    stock = get_object_or_404(

        Stock,

        pk=pk,

    )

    if request.method == "POST":

        form = StockForm(

            request.POST,

            instance=stock,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Stock updated successfully."

            )

            return redirect(

                "inventory:stock_list"

            )

    else:

        form = StockForm(

            instance=stock,

        )

    context = {

        "form": form,

        "title": "Edit Stock",

    }

    return render(

        request,

        "inventory/stock_form.html",

        context,

    )
# ==========================================================
# STOCK DELETE
# ==========================================================

@login_required(login_url="login")
def stock_delete(request, pk):

    stock = get_object_or_404(

        Stock,

        pk=pk,

    )

    if request.method == "POST":

        stock.delete()

        messages.success(

            request,

            "Stock deleted successfully."

        )

    return redirect(

        "inventory:stock_list"

    )

    stock = get_object_or_404(

        Stock,

        pk=pk,

    )

    if request.method == "POST":

        stock.delete()

        messages.success(

            request,

            "Stock deleted successfully."

        )

    return redirect(

        "inventory:stock_list"

    )        
# ==========================================================
# STOCK MOVEMENT LIST
# ==========================================================

@login_required(login_url="login")
def stock_movement_list(request):

    search = request.GET.get(

        "search",

        ""

    )

    movements = StockMovement.objects.select_related(

        "stock",

        "stock__product",

        "stock__warehouse",

    )

    if search:

        movements = movements.filter(

            stock__product__name__icontains=search

        )

    context = {

        "movements": movements.order_by(

            "-id"

        ),

        "search": search,

    }

    return render(

        request,

        "inventory/stock_movement_list.html",

        context,

    )

    return render(

        request,

        "inventory/stock_movement_list.html",

    )
@login_required(login_url="login")
def stock_movement_create(request):
    if request.method == "POST":
        form = StockMovementForm(request.POST)

        if form.is_valid():
            movement = form.save(commit=False)
            movement.created_by = request.user

            stock = movement.stock

            if movement.movement_type == "IN":
                stock.quantity += movement.quantity

            elif movement.movement_type == "OUT":
                stock.quantity -= movement.quantity

            elif movement.movement_type == "ADJUSTMENT":
                stock.quantity = movement.quantity

            stock.available_quantity = (
                stock.quantity - stock.reserved_quantity
            )

            stock.save()
            movement.save()

            messages.success(
                request,
                "Stock movement added successfully."
            )

            return redirect("inventory:stock_movement_list")

    else:
        form = StockMovementForm()

    return render(
        request,
        "inventory/stock_movement_form.html",
        {
            "form": form,
            "title": "Add Stock Movement",
        },
    )

    if request.method == "POST":

        form = StockMovementForm(

            request.POST,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Stock movement added successfully."

            )

            return redirect(

                "inventory:stock_movement_list"

            )

    else:

        form = StockMovementForm()

    context = {

        "form": form,

        "title": "Add Stock Movement",

    }

    return render(

        request,

        "inventory/stock_movement_form.html",

        context,

    )

    return render(

        request,

        "inventory/stock_movement_form.html",

    )  
@login_required(login_url="login")
def stock_movement_update(request, pk):
    movement = get_object_or_404(
        StockMovement,
        pk=pk,
    )

    if request.method == "POST":
        old_stock = movement.stock
        old_type = movement.movement_type
        old_quantity = movement.quantity

        form = StockMovementForm(
            request.POST,
            instance=movement,
        )

        if form.is_valid():
            updated = form.save(commit=False)
            updated.created_by = movement.created_by

            if old_type == "IN":
                old_stock.quantity -= old_quantity

            elif old_type == "OUT":
                old_stock.quantity += old_quantity

            old_stock.available_quantity = (
                old_stock.quantity - old_stock.reserved_quantity
            )
            old_stock.save()

            new_stock = updated.stock

            if updated.movement_type == "IN":
                new_stock.quantity += updated.quantity

            elif updated.movement_type == "OUT":
                new_stock.quantity -= updated.quantity

            elif updated.movement_type == "ADJUSTMENT":
                new_stock.quantity = updated.quantity

            new_stock.available_quantity = (
                new_stock.quantity - new_stock.reserved_quantity
            )
            new_stock.save()

            updated.save()

            messages.success(
                request,
                "Stock movement updated successfully."
            )

            return redirect("inventory:stock_movement_list")

    else:
        form = StockMovementForm(instance=movement)

    return render(
        request,
        "inventory/stock_movement_form.html",
        {
            "form": form,
            "title": "Edit Stock Movement",
        },
    )

    movement = get_object_or_404(

        StockMovement,

        pk=pk,

    )

    if request.method == "POST":

        form = StockMovementForm(

            request.POST,

            instance=movement,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Stock movement updated successfully."

            )

            return redirect(

                "inventory:stock_movement_list"

            )

    else:

        form = StockMovementForm(

            instance=movement,

        )

    context = {

        "form": form,

        "title": "Edit Stock Movement",

    }

    return render(

        request,

        "inventory/stock_movement_form.html",

        context,

    )  
@login_required(login_url="login")
def stock_movement_delete(request, pk):
    movement = get_object_or_404(
        StockMovement,
        pk=pk,
    )

    if request.method == "POST":
        stock = movement.stock

        if movement.movement_type == "IN":
            stock.quantity -= movement.quantity

        elif movement.movement_type == "OUT":
            stock.quantity += movement.quantity

        elif movement.movement_type == "ADJUSTMENT":
            pass

        stock.available_quantity = (
            stock.quantity - stock.reserved_quantity
        )

        stock.save()

        movement.delete()

        messages.success(
            request,
            "Stock movement deleted successfully."
        )

    return redirect("inventory:stock_movement_list")

    movement = get_object_or_404(

        StockMovement,

        pk=pk,

    )

    if request.method == "POST":

        movement.delete()

        messages.success(

            request,

            "Stock movement deleted successfully."

        )

    return redirect(

        "inventory:stock_movement_list"

    )                                          
# ==========================================================
# PRODUCT CREATE
# ==========================================================


@login_required(login_url="login")
def product_create(request):

    if request.method == "POST":

        form = ProductForm(

            request.POST,

            request.FILES,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Product created successfully."

            )

            return redirect(

                "inventory:product_list"

            )

    else:

        form = ProductForm()

    context = {

        "form": form,

        "title": "Add Product",

    }

    return render(

        request,

        "inventory/product_form.html",

        context,

    )

    if request.method == "POST":

        # Product save logic will be implemented
        # after Category, Brand and Unit modules
        # are completed.

        messages.success(

            request,

            "Product page is connected successfully."

        )

        return redirect(

            "inventory:product_list"

        )

    context = {

        "categories": Category.objects.filter(

            is_active=True

        ).order_by(

            "name"

        ),

        "brands": Brand.objects.filter(

            is_active=True

        ).order_by(

            "name"

        ),

        "units": Unit.objects.filter(

            is_active=True

        ).order_by(

            "name"

        ),

    }

    return render(

        request,

        "inventory/product_form.html",

        context,

    )
# ==========================================================
# PRODUCT UPDATE
# ==========================================================

@login_required(login_url="login")
def product_update(request, pk):

    product = get_object_or_404(

        Product,

        pk=pk,

    )

    if request.method == "POST":

        form = ProductForm(

            request.POST,

            request.FILES,

            instance=product,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Product updated successfully."

            )

            return redirect(

                "inventory:product_list"

            )

    else:

        form = ProductForm(

            instance=product,

        )

    context = {

        "form": form,

        "title": "Edit Product",

    }

    return render(

        request,

        "inventory/product_form.html",

        context,

    )   
# ==========================================================
# PRODUCT DELETE
# ==========================================================

@login_required(login_url="login")
def product_delete(request, pk):

    product = get_object_or_404(

        Product,

        pk=pk,

    )

    if request.method == "POST":

        product.delete()

        messages.success(

            request,

            "Product deleted successfully."

        )

    return redirect(

        "inventory:product_list"

    )     


# ==========================================================
# END OF FILE
# ==========================================================    