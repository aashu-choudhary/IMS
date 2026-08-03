from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .forms import CustomerForm
from .models import Customer


# ==========================================================
# CUSTOMER DASHBOARD
# ==========================================================

@login_required(login_url="login")
def customer_dashboard(request):

    total_customers = Customer.objects.count()

    active_customers = Customer.objects.filter(
        is_active=True
    ).count()

    inactive_customers = Customer.objects.filter(
        is_active=False
    ).count()

    total_credit = Customer.objects.aggregate(
        total=Sum("credit_limit")
    )["total"] or 0

    total_outstanding = Customer.objects.aggregate(
        total=Sum("outstanding_balance")
    )["total"] or 0

    context = {

        "total_customers": total_customers,

        "active_customers": active_customers,

        "inactive_customers": inactive_customers,

        "total_credit": total_credit,

        "total_outstanding": total_outstanding,

        # Sales module integration later
        "total_orders": 0,

    }

    return render(

        request,

        "customers/dashboard.html",

        context,

    )


# ==========================================================
# CUSTOMER LIST
# ==========================================================

@login_required(login_url="login")
def customer_list(request):

    search = request.GET.get(

        "search",

        ""

    ).strip()

    status = request.GET.get(

        "status",

        ""

    )

    customers = Customer.objects.all()

    if search:

        customers = customers.filter(

            Q(customer_code__icontains=search)

            |

            Q(name__icontains=search)

            |

            Q(company_name__icontains=search)

            |

            Q(phone__icontains=search)

            |

            Q(email__icontains=search)

            |

            Q(city__icontains=search)

            |

            Q(gst_number__icontains=search)

        )

    if status == "active":

        customers = customers.filter(

            is_active=True

        )

    elif status == "inactive":

        customers = customers.filter(

            is_active=False

        )

    customers = customers.order_by(

        "name"

    )

    context = {

        "customers": customers,

        "search": search,

        "selected_status": status,

        "total_customers": customers.count(),

        "active_customers": customers.filter(
            is_active=True
        ).count(),

        "inactive_customers": customers.filter(
            is_active=False
        ).count(),

        "total_credit": sum(
            customer.credit_limit
            for customer in customers
        ),

        "total_outstanding": sum(
            customer.outstanding_balance
            for customer in customers
        ),

    }

    return render(

        request,

        "customers/customer_list.html",

        context,

    )


# ==========================================================
# CUSTOMER VIEW
# ==========================================================

@login_required(login_url="login")
def customer_view(request, pk):

    customer = get_object_or_404(

        Customer,

        pk=pk,

    )

    context = {

        "customer": customer,

    }

    return render(

        request,

        "customers/customer_view.html",

        context,

    )
# ==========================================================
# ADD CUSTOMER
# ==========================================================

@login_required(login_url="login")
def customer_create(request):

    if request.method == "POST":

        form = CustomerForm(request.POST)

        if form.is_valid():

            customer = form.save(commit=False)

            customer.outstanding_balance = (

                customer.opening_balance

            )

            customer.save()

            messages.success(

                request,

                "Customer added successfully."

            )

            return redirect(

                "customers:customer_list"

            )

        else:

            messages.error(

                request,

                "Please correct the errors below."

            )

    else:

        form = CustomerForm()

    context = {

        "form": form,

    }

    return render(

        request,

        "customers/customer_create.html",

        context,

    )

    if request.method == "POST":

        form = CustomerForm(

            request.POST

        )

        if form.is_valid():

            customer = form.save(

                commit=False

            )

            # Initial Outstanding Balance

            customer.outstanding_balance = (

                customer.opening_balance

            )

            customer.save()

            messages.success(

                request,

                "Customer added successfully."

            )

            return redirect(

                "customers:customer_list"

            )

    else:

        form = CustomerForm()

    context = {

        "form": form,

        "title": "Add Customer",

    }

    return render(

        request,

        "customers/customer_create.html",

        context,

    )


# ==========================================================
# UPDATE CUSTOMER
# ==========================================================

@login_required(login_url="login")
def customer_update(request, pk):

    customer = get_object_or_404(

        Customer,

        pk=pk,

    )

    if request.method == "POST":

        form = CustomerForm(

            request.POST,

            instance=customer,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Customer updated successfully."

            )

            return redirect(

                "customers:customer_list"

            )

    else:

        form = CustomerForm(

            instance=customer,

        )

    context = {

        "form": form,

        "customer": customer,

        "title": "Edit Customer",

    }

    return render(

        request,

        "customers/customer_create.html",

        context,

    )


# ==========================================================
# DELETE CUSTOMER
# ==========================================================

@login_required(login_url="login")
def customer_delete(request, pk):

    customer = get_object_or_404(

        Customer,

        pk=pk,

    )

    if request.method == "POST":

        customer.delete()

        messages.success(

            request,

            "Customer deleted successfully."

        )

    return redirect(

        "customers:customer_list"

    )    
# ==========================================================
# EDIT CUSTOMER
# ==========================================================

@login_required(login_url="login")
def customer_edit(request, pk):

    customer = get_object_or_404(

        Customer,

        pk=pk,

    )

    return render(

        request,

        "customers/customer_edit.html",

        {

            "customer": customer,

        },

    )    
# ==========================================================
# EDIT CUSTOMER
# ==========================================================

@login_required(login_url="login")
def customer_edit(request, pk):

    customer = get_object_or_404(

        Customer,

        pk=pk,

    )

    if request.method == "POST":

        form = CustomerForm(

            request.POST,

            instance=customer,

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Customer updated successfully."

            )

            return redirect(

                "customers:customer_list"

            )

        else:

            messages.error(

                request,

                "Please correct the errors below."

            )

    else:

        form = CustomerForm(

            instance=customer,

        )

    context = {

        "customer": customer,

        "form": form,

        "title": "Edit Customer",

    }

    return render(

        request,

        "customers/customer_edit.html",

        context,

    )
# ==========================================================
# DELETE CUSTOMER
# ==========================================================

@login_required(login_url="login")
def customer_delete(request, pk):

    customer = get_object_or_404(

        Customer,

        pk=pk,

    )

    if request.method == "POST":

        customer_name = customer.name

        customer.delete()

        messages.success(

            request,

            f"Customer '{customer_name}' deleted successfully."

        )

    return redirect(

        "customers:customer_list"

    )

    customer = get_object_or_404(

        Customer,

        pk=pk,

    )

    if request.method == "POST":

        customer.delete()

        messages.success(

            request,

            "Customer deleted successfully."

        )

    return redirect(

        "customers:customer_list"

    )        