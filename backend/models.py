from cgi import print_arguments

from django.db import models

# Create your models here.
class Category(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        db_table='category'

class Brand(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255)
    image_path=models.ImageField(upload_to='brand',null=True,blank=True,default="no_image_available.png")

    def __str__(self):
        return self.name
    class Meta:
        db_table='brand'

class Product(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        db_table='product'

class Cart(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        db_table='cart'

class Order(models.Model):
    id=models.BigAutoField(primary_key=True)
    order_number = models.CharField(max_length=255,blank=True,null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.order_number
    class Meta:
        db_table='order'

class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    qty = models.IntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.IntegerField(blank=True,null=True,default=0)

    def __str__(self):
        return self.id
    class Meta:
        db_table='order_Item'


