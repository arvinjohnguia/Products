from django.db import models

# Create your models here.
class IsActiveManager(models.Manager):
    def get_queryset(self):

        return super(IsActiveManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    Cat_Name = models.CharField(max_length=200, verbose_name="Category")

    def __str__(self):
        return self.Cat_Name

#class ProductType(models.Model):
#    ProdType_Name = models.CharField(max_length=200, verbose_name="Product Type")

#    def __str__(self):
#        return self.ProdType_Name

class Product(models.Model):
    insProd_Name = models.CharField(max_length=200, verbose_name="Product Name")
    Cat_Name = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Category")
    #ProdType_Name = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Category")
    insProd_Desc = models.TextField(max_length=200, null=True, blank=True, verbose_name="Description")
    insProd_stockQty = models.IntegerField(verbose_name="Stock Quantity")
    insProd_Price = models.FloatField(verbose_name="Price")
    insProd_Image = models.ImageField(default="placeholder-image.png", upload_to="product_images", null=True, verbose_name="Product Image")
    is_active = models.BooleanField(default=True, verbose_name="Status")
    objects = models.Manager() #For All Records  
    active_objects = IsActiveManager() #For Active Records Only
    #insProd_totalUsed = models.IntegerField(verbose_name="Total Used")
    #insProd_dateRestocked = models.DateTimeField(auto_now=True)
    #insProd_DateUsed

    def __str__(self):
        return self.insProd_Name
