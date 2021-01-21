from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save

from account.models import Account

from mysite.utils import unique_slug_generator


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance) 

class Product(models.Model):
    category = models.CharField(max_length=50, blank=False, null=False)
    marketing = models.BooleanField(default=False)
    marketing_image = models.ImageField(upload_to='pictures/', blank=True, null=True)
    new_arrival = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    sale_off = models.BooleanField(default=False)
    name = models.CharField(max_length=300, null=False, blank=False)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False)
    discount_price = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=False, blank=False)
    description = models.TextField(blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    operation_system = models.CharField(max_length=300, blank=True)
    pc_model = models.CharField(max_length=300, blank=True)
    appearance = models.CharField(max_length=300, blank=True)
    display = models.CharField(max_length=300, blank=True)
    display_definition = models.CharField(max_length=300, blank=True)
    display_covering = models.CharField(max_length=300, blank=True)
    cpu_name = models.CharField(max_length=300, blank=True)
    cpu_model = models.CharField(max_length=300, blank=True)
    cpu_core = models.CharField(max_length=300, blank=True)
    cpu_freq = models.CharField(max_length=300, blank=True)
    operation_memory = models.CharField(max_length=300, blank=True)
    gpu = models.CharField(max_length=300, blank=True)
    memory = models.CharField(max_length=300, blank=True)
    camera = models.CharField(max_length=300, blank=True)
    peripheral = models.CharField(max_length=300, blank=True)
    battery_capacity = models.CharField(max_length=300, blank=True)
    battery_power = models.CharField(max_length=300, blank=True)
    process_time = models.CharField(max_length=300, blank=True)
    depth = models.CharField(max_length=300, blank=True)
    height = models.CharField(max_length=300, blank=True)
    width = models.CharField(max_length=300, blank=True)
    weight = models.CharField(max_length=300, blank=True)
    published = models.DateTimeField('publishing date')
    slug = models.SlugField(null=True, blank=True)
    image = models.FileField(upload_to='pictures/', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('product_detailed_view', kwargs={'slug': self.slug})


class ProductImage(models.Model):
    product_detailed = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='pictures/')

    def __str__(self):
        return self.product_detailed.name


pre_save.connect(slug_generator, sender=Product)

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', null=False)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name

class ViewedProduct(models.Model):
    viewed_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    session = models.CharField(max_length=10000, blank=True, null=True)
    date = models.DateTimeField('date')

    def __str__(self):
        return str(self.id)

class NewArrival(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='marketing_category/')

    def __str__(self):
        return self.name

class Discount(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='marketing_category/')

    def __str__(self):
        return self.name

class SaleOff(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='marketing_category/')

    def __str__(self):
        return self.name