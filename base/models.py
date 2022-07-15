from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#PRODUCTS MODELS ------------------------------------------------------
class IsActiveManager(models.Manager):
    def get_queryset(self):

        return super(IsActiveManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    Cat_Name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.Cat_Name

class ProductType(models.Model):
    ProdType_Name = models.CharField(max_length=200, verbose_name="Product Type", unique=True)

    def __str__(self):
        return self.ProdType_Name

class insProduct(models.Model):
    Prod_Name = models.CharField(max_length=200, verbose_name="Product Name")
    ProdType_Name = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Product Type")
    Cat_Name = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Category")
    Prod_Desc = models.TextField(max_length=200, null=True, blank=True, verbose_name="Description")
    Prod_stockQty = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Stock Quantity")
    Prod_Price = models.FloatField(verbose_name="Price")
    Prod_Image = models.ImageField(default="placeholder-image.png", upload_to="product_images", null=True, verbose_name="Product Image")
    is_active = models.BooleanField(default=True, verbose_name="Status")
    objects = models.Manager() #For All Records  
    active_objects = IsActiveManager() #For Active Records Only
    date_created = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(null=True, blank=False)
    #insProd_totalUsed = models.IntegerField(verbose_name="Total Used")
    #insProd_dateRestocked = models.DateTimeField(auto_now=True)
    #insProd_DateUsed

    class Meta:
        verbose_name = 'In-salon Product'

    def __str__(self):
        return self.Prod_Name

class otcProduct(models.Model):
    Prod_Name = models.CharField(max_length=200, verbose_name="Product Name")
    ProdType_Name = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Product Type")
    Cat_Name = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Category")
    Prod_Desc = models.TextField(max_length=200, null=True, blank=True, verbose_name="Description")
    Prod_stockQty = models.IntegerField(verbose_name="Stock Quantity")
    Prod_Price = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Price")
    Prod_Image = models.ImageField(default="placeholder-image.png", upload_to="product_images", null=True, verbose_name="Product Image")
    is_active = models.BooleanField(default=True, verbose_name="Status")
    objects = models.Manager() #For All Records  
    active_objects = IsActiveManager() #For Active Records Only
    date_created = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(null=True, blank=False)

    class Meta:
        verbose_name = 'Over-the-Counter Product'

    def __str__(self):
        return self.Prod_Name

#ECOMMERCE MODELS ------------------------------------------------------

class Customer(models.Model):
    #A user can only have one customer. Customer can only have one user
    #Keep the on_delete=models.CASCADE for now; change later
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

'''class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()

    #For digital products that won't be shipped
    #Can change later

    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
'''

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(otcProduct, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.Prod_Price * self.quantity
        return total

# PRODUCT PICKUP
class Checkout(models.Model):
    cname = 

class PickupStatus(models.Model):
    pickup_status = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Product Pickup Status'
        verbose_name_plural = 'Product Pickup Statuses'

    def __str__(self):
        return self.pickup_status
    
class ProductPickup(models.Model):
    product = models.ForeignKey(otcProduct, on_delete=models.SET_NULL, blank=False, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=False, null=True)
    pickupstat = models.ForeignKey(PickupStatus, blank=False, null=True)
    pickUp_Date = models.DateTimeField(null=True, blank=False, verbose_name="Pickup Date")
    pickUpProd_Qty = models.IntegerField(verbose_name="Pickup Product Quantity")


class SalesInvoice(models.Model):
    product_pickup = models.ForeignKey(ProductPickup, blank=False, null=True)
    amount_total = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Total Price")