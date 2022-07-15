from django.contrib import admin

# Register your models here.

admin.site.site_header = "SalOnTheGo Admin"
admin.site.site_title = "SalOnTheGo Admin"
#admin.site.index_title = "Welcome to "

from .models import Product, ProductType, Category

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Category)