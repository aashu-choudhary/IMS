from django import forms

from .models import Supplier


# ==========================================================
# SUPPLIER FORM
# ==========================================================

class SupplierForm(forms.ModelForm):

    class Meta:

        model = Supplier

        fields = [

            "supplier_code",

            "name",

            "company_name",

            "phone",

            "email",

            "is_active",

        ]

        widgets = {

            "supplier_code": forms.TextInput(

                attrs={

                    "placeholder": "Supplier Code",

                }

            ),

            "name": forms.TextInput(

                attrs={

                    "placeholder": "Supplier Name",

                }

            ),

            "company_name": forms.TextInput(

                attrs={

                    "placeholder": "Company Name",

                }

            ),

            "phone": forms.TextInput(

                attrs={

                    "placeholder": "Phone Number",

                }

            ),

            "email": forms.EmailInput(

                attrs={

                    "placeholder": "Email Address",

                }

            ),

        }