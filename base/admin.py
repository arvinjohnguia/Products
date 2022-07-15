from django.contrib import admin

# Register your models here.

admin.site.site_header = "SalOnTheGo Admin"
admin.site.site_title = "SalOnTheGo Admin"
#admin.site.index_title = "Welcome to "

from .models import * #insProduct, otcProduct, ProductType, Category

admin.site.register(insProduct)
admin.site.register(otcProduct)
admin.site.register(ProductType)
admin.site.register(Category)

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
#admin.site.register(ShippingAddress)