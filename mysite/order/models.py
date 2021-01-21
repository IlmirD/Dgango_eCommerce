from django.db import models
from account.models import Account
from product.models import Product


# ORDER
class Order(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    date_ordered = models.DateTimeField(auto_now_add=True,)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        ordering = ('-date_ordered',)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.order_item.all()
        for i in orderitems:
            if not i.product.digital:
                shipping = True
        return shipping


# OrderItem
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, related_name='order_item', on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    line_total = models.DecimalField(default=0, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        try:
            return self.product.name
        except:
            return self.product.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    region = models.CharField(max_length=300, null=False, default="")
    district = models.CharField(max_length=300, null=False, default="")
    city = models.CharField(max_length=300, null=False, default="")
    zip_code = models.CharField(max_length=300, null=False, default="")
    street = models.CharField(max_length=300, null=False, default="")
    house = models.CharField(max_length=300, null=False, default="")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.region