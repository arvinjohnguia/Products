from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['insProd_Name', 'Cat_Name', 'insProd_Desc', 'insProd_stockQty', 'insProd_Price', 'insProd_Image', 'is_active']


