from django.db import models

# Create your models here.

class Product(models.Model):
    insProd_Name = models.CharField(max_length=200, verbose_name="Product Name")
    insProd_Desc = models.TextField(null=True, blank=True, verbose_name="Description")
    insProd_stockQty = models.IntegerField(verbose_name="Stock Quantity")
    insProd_Price = models.FloatField(verbose_name="Price")
    #insProd_totalUsed = models.IntegerField(verbose_name="Total Used")
    #insProd_dateRestocked = models.DateTimeField(auto_now=True)
    #insProd_DateUsed


    def __str__(self):
        return self.insProd_Name