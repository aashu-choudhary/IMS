from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import SupplierForm

# ==========================================================
# SUPPLIER DASHBOARD
# ==========================================================

@login_required(login_url="login")
def dashboard(request):

    return render(

        request,

        "suppliers/dashboard.html",

    )
from django.shortcuts import render


# ==========================================================
# SUPPLIER LIST
# ==========================================================

from .models import Supplier


# ==========================================================
# SUPPLIER LIST
# ==========================================================

def supplier_list(request):

    suppliers = (

        Supplier.objects

        .all()

        .order_by("name")

    )

    context = {

        "suppliers": suppliers,

    }

    return render(

        request,

        "suppliers/supplier_list.html",

        context,

    )
# ==========================================================
# ADD SUPPLIER
# ==========================================================
from django.shortcuts import render, redirect
from .forms import SupplierForm


# ==========================================================
# ADD SUPPLIER
# ==========================================================

def supplier_create(request):

    if request.method == "POST":

        form = SupplierForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("suppliers:supplier_list")

    else:

        form = SupplierForm()

    return render(

        request,

        "suppliers/supplier_create.html",

        {

            "form": form,

        },

    )

    if request.method == "POST":

        form = SupplierForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(

                "suppliers:supplier_list"

            )

    else:

        form = SupplierForm()

    return render(

        request,

        "suppliers/supplier_form.html",

        {

            "form": form,

        },

    )  
from django.shortcuts import render, redirect, get_object_or_404

from .models import Supplier
from .forms import SupplierForm


# ==========================================================
# EDIT SUPPLIER
# ==========================================================

def supplier_edit(request, pk):

    supplier = get_object_or_404(

        Supplier,

        pk=pk

    )

    if request.method == "POST":

        form = SupplierForm(

            request.POST,

            instance=supplier

        )

        if form.is_valid():

            form.save()

            return redirect(

                "suppliers:supplier_list"

            )

    else:

        form = SupplierForm(

            instance=supplier

        )

    return render(

        request,

        "suppliers/supplier_edit.html",

        {

            "form": form,

            "supplier": supplier,

        }

    )
    supplier = get_object_or_404(

        Supplier,

        pk=pk

    )

    if request.method == "POST":

        form = SupplierForm(

            request.POST,

            instance=supplier

        )

        if form.is_valid():

            form.save()

            return redirect(

                "suppliers:supplier_list"

            )

    else:

        form = SupplierForm(

            instance=supplier

        )

    return render(

        request,

        "suppliers/supplier_edit.html",

        {

            "form": form,

            "supplier": supplier,

        }

    )
# ==========================================================
# DELETE SUPPLIER
# ==========================================================

# ==========================================================
# DELETE SUPPLIER
# ==========================================================

def supplier_delete(request, pk):

    supplier = get_object_or_404(

        Supplier,

        pk=pk

    )

    supplier.delete()

    return redirect(

        "suppliers:supplier_list"

    )

    supplier = get_object_or_404(

        Supplier,

        pk=pk

    )

    supplier.delete()

    return redirect(

        "suppliers:supplier_list"

    )          