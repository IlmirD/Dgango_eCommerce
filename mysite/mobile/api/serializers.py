from rest_framework import serializers
from mobile.models import ProductCategory, MarketingCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['name', 'image']

class MarketingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingCategory
        fields = ['name', 'image']