from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='mobile/')

    def __str__(self):
        return self.name

class MarketingCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='mobile/')

    def __str__(self):
        return self.name