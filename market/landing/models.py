from django.db import models

# Create your models here.

class Order(models.Model):

    #personal information
    name = models.CharField(max_length=26)
    number = models.BigIntegerField()
    alternative_number = models.BigIntegerField(null=True,blank=True)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    zip = models.CharField(max_length=300)
    amount = models.IntegerField(default = 0)
    product_code = models.CharField(max_length=300,null=True,blank=True)

    #Payment mode cod or ppd
    payment_mode = models.CharField(max_length=300 ,null=True ,blank = True)
    # payment status for development
    payment_status = models.BooleanField(default=False)
   
    
    #order status
    order_id = models.CharField(max_length=300 ,null=True ,blank = True)
    # order dispach or not
    order_status_pending = models.BooleanField(default=True)
    # order deliver status
    order_status_deliverd = models.BooleanField(default=False)
    # order failed status
    order_status_failed = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)