from django.forms import ModelForm #,CheckboxInput
from django import forms
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['insProd_Name', 'Cat_Name', 'insProd_Desc', 'insProd_stockQty', 'insProd_Price', 'insProd_Image', 'is_active']

class StatusForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_active']

        #widgets = {
        #    'is_active': CheckboxInput(attrs={'onchange': 'this.form.submit();'})
        #}