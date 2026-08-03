from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer

        fields = [
            "customer_code",
            "customer_type",
            "name",
            "company_name",
            "email",
            "phone",
            "alternate_phone",
            "gst_number",
            "pan_number",
            "address",
            "city",
            "state",
            "country",
            "postal_code",
            "credit_limit",
            "opening_balance",
            "outstanding_balance",
            "is_active",
            "notes",
        ]

        widgets = {

            "customer_code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Customer Code",
            }),

            "customer_type": forms.Select(attrs={
                "class": "form-control",
            }),

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Customer Name",
            }),

            "company_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Name",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email",
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number",
            }),

            "alternate_phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Alternate Phone",
            }),

            "gst_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "GST Number",
            }),

            "pan_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "PAN Number",
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Address",
            }),

            "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "City",
            }),

            "state": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "State",
            }),

            "country": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Country",
            }),

            "postal_code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Postal Code",
            }),

            "credit_limit": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
            }),

            "opening_balance": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
            }),
"outstanding_balance": forms.NumberInput(

    attrs={

        "class": "form-control",

        "step": "0.01",

    }

),
            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),

            "notes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Additional Notes",
            }),
        }