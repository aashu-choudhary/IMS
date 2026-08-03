from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = [

            "name",

            "description",

            "is_active",

        ]

        widgets = {

            "name": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter category name",

                }

            ),

            "description": forms.Textarea(

                attrs={

                    "class": "form-control",

                    "rows": 4,

                    "placeholder": "Enter category description",

                }

            ),

            "is_active": forms.CheckboxInput(

                attrs={

                    "class": "form-check-input",

                }

            ),

        }

        labels = {

            "name": "Category Name",

            "description": "Description",

            "is_active": "Active",

        }

        help_texts = {

            "name": "",

            "description": "",

        }

    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        if Category.objects.filter(name__iexact=name).exists():

            if not self.instance.pk:

                raise forms.ValidationError(

                    "Category already exists."

                )

            elif Category.objects.filter(

                name__iexact=name

            ).exclude(

                pk=self.instance.pk

            ).exists():

                raise forms.ValidationError(

                    "Category already exists."

                )

        return name
    
from .models import Brand


class BrandForm(forms.ModelForm):

    class Meta:

        model = Brand

        fields = [

            "name",

            "description",

            "is_active",

        ]

        widgets = {

            "name": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter Brand Name",

                }

            ),

            "description": forms.Textarea(

                attrs={

                    "class": "form-control",

                    "rows": 4,

                    "placeholder": "Enter Brand Description",

                }

            ),

            "is_active": forms.CheckboxInput(

                attrs={

                    "class": "form-check-input",

                }

            ),

        }

    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        if Brand.objects.filter(

            name__iexact=name

        ).exclude(

            pk=self.instance.pk

        ).exists():

            raise forms.ValidationError(

                "Brand already exists."

            )

        return name 
# ==========================================================
# UNIT FORM
# ==========================================================

from .models import Unit


class UnitForm(forms.ModelForm):

    class Meta:

        model = Unit

        fields = [

            "name",

            "short_name",

            "description",

            "is_active",

        ]

        widgets = {

            "name": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter Unit Name",

                }

            ),

            "short_name": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter Short Name",

                }

            ),

            "description": forms.Textarea(

                attrs={

                    "class": "form-control",

                    "rows": 4,

                    "placeholder": "Enter Unit Description",

                }

            ),

            "is_active": forms.CheckboxInput(

                attrs={

                    "class": "form-check-input",

                }

            ),

        }


    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        queryset = Unit.objects.filter(

            name__iexact=name

        )

        if self.instance.pk:

            queryset = queryset.exclude(

                pk=self.instance.pk

            )

        if queryset.exists():

            raise forms.ValidationError(

                "Unit already exists."

            )

        return name


    def clean_short_name(self):

        short_name = self.cleaned_data["short_name"].strip()

        queryset = Unit.objects.filter(

            short_name__iexact=short_name

        )

        if self.instance.pk:

            queryset = queryset.exclude(

                pk=self.instance.pk

            )

        if queryset.exists():

            raise forms.ValidationError(

                "Short Name already exists."

            )

        return short_name       
# ==========================================================
# WAREHOUSE FORM
# ==========================================================

from .models import Warehouse


class WarehouseForm(forms.ModelForm):

    class Meta:

        model = Warehouse

        fields = [

            "name",

            "code",

            "address",

            "city",

            "state",

            "country",

            "contact_person",

            "contact_number",

            "is_active",

        ]

        widgets = {

            "name": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter Warehouse Name",

                }

            ),

            "code": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter Warehouse Code",

                }

            ),

            "address": forms.Textarea(

                attrs={

                    "class": "form-control",

                    "rows": 3,

                    "placeholder": "Enter Address",

                }

            ),

            "city": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter City",

                }

            ),

            "state": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter State",

                }

            ),

            "country": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter Country",

                }

            ),

            "contact_person": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter Contact Person",

                }

            ),

            "contact_number": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter Contact Number",

                }

            ),

            "is_active": forms.CheckboxInput(

                attrs={

                    "class": "form-check-input",

                }

            ),

        }


    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        queryset = Warehouse.objects.filter(

            name__iexact=name

        )

        if self.instance.pk:

            queryset = queryset.exclude(

                pk=self.instance.pk

            )

        if queryset.exists():

            raise forms.ValidationError(

                "Warehouse already exists."

            )

        return name


    def clean_code(self):

        code = self.cleaned_data["code"].strip()

        queryset = Warehouse.objects.filter(

            code__iexact=code

        )

        if self.instance.pk:

            queryset = queryset.exclude(

                pk=self.instance.pk

            )

        if queryset.exists():

            raise forms.ValidationError(

                "Warehouse code already exists."

            )

        return code
# ==========================================================
# PRODUCT FORM
# ==========================================================

from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = [

            "sku",

            "name",

            "category",

            "brand",

            "unit",

            "description",

            "image",

            "purchase_price",

            "selling_price",

            "barcode",

            "is_active",

        ]

        widgets = {

            "sku": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter SKU",

                }

            ),

            "name": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter Product Name",

                }

            ),

            "category": forms.Select(

                attrs={

                    "class": "form-control",

                }

            ),

            "brand": forms.Select(

                attrs={

                    "class": "form-control",

                }

            ),

            "unit": forms.Select(

                attrs={

                    "class": "form-control",

                }

            ),

            "description": forms.Textarea(

                attrs={

                    "class": "form-control",

                    "rows": 4,

                    "placeholder": "Enter Description",

                }

            ),

            "image": forms.ClearableFileInput(

                attrs={

                    "class": "form-control",

                }

            ),

            "purchase_price": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "step": "0.01",

                }

            ),

            "selling_price": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "step": "0.01",

                }

            ),

            "barcode": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter Barcode",

                }

            ),

            "is_active": forms.CheckboxInput(

                attrs={

                    "class": "form-check-input",

                }

            ),

        }


    def clean_sku(self):

        sku = self.cleaned_data["sku"].strip()

        queryset = Product.objects.filter(

            sku__iexact=sku

        )

        if self.instance.pk:

            queryset = queryset.exclude(

                pk=self.instance.pk

            )

        if queryset.exists():

            raise forms.ValidationError(

                "SKU already exists."

            )

        return sku


    def clean_barcode(self):

        barcode = self.cleaned_data.get("barcode")

        if barcode:

            barcode = barcode.strip()

            queryset = Product.objects.filter(

                barcode__iexact=barcode

            )

            if self.instance.pk:

                queryset = queryset.exclude(

                    pk=self.instance.pk

                )

            if queryset.exists():

                raise forms.ValidationError(

                    "Barcode already exists."

                )

        return barcode
# ==========================================================
# STOCK FORM
# ==========================================================

from .models import Stock


class StockForm(forms.ModelForm):

    class Meta:

        model = Stock

        fields = [

            "product",

            "warehouse",

            "quantity",

            "reserved_quantity",

            "available_quantity",

            "minimum_stock",

            "maximum_stock",

            "reorder_level",

        ]

        widgets = {

            "product": forms.Select(

                attrs={

                    "class": "form-control",

                }

            ),

            "warehouse": forms.Select(

                attrs={

                    "class": "form-control",

                }

            ),

            "quantity": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "min": 0,

                }

            ),

            "reserved_quantity": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "min": 0,

                }

            ),

            "available_quantity": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "min": 0,

                }

            ),

            "minimum_stock": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "min": 0,

                }

            ),

            "maximum_stock": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "min": 0,

                }

            ),

            "reorder_level": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "min": 0,

                }

            ),

        }

    def clean(self):

        cleaned_data = super().clean()

        product = cleaned_data.get("product")

        warehouse = cleaned_data.get("warehouse")

        if product and warehouse:

            queryset = Stock.objects.filter(

                product=product,

                warehouse=warehouse,

            )

            if self.instance.pk:

                queryset = queryset.exclude(

                    pk=self.instance.pk,

                )

            if queryset.exists():

                raise forms.ValidationError(

                    "This product already exists in the selected warehouse."

                )

        return cleaned_data    
# ==========================================================
# STOCK MOVEMENT FORM
# ==========================================================

from .models import StockMovement


class StockMovementForm(forms.ModelForm):

    class Meta:

        model = StockMovement

        fields = [

            "stock",

            "movement_type",

            "quantity",

            "reference_number",

            "remarks",

        ]

        widgets = {

            "stock": forms.Select(

                attrs={

                    "class": "form-control",

                }

            ),

            "movement_type": forms.Select(

                attrs={

                    "class": "form-control",

                }

            ),

            "quantity": forms.NumberInput(

                attrs={

                    "class": "form-control",

                    "min": 1,

                }

            ),

           "reference_number": forms.TextInput(

    attrs={

        "class": "form-control",

        "placeholder": "Reference Number",

    }

),

            "remarks": forms.Textarea(

                attrs={

                    "class": "form-control",

                    "rows": 4,

                    "placeholder": "Remarks",

                }

            ),

        }            