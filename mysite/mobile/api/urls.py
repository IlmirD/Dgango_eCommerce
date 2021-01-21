from django.urls import path


from mobile.api.views import (
    ApiProductCategory,
    ApiMarketingCategory,
)

urlpatterns = [
    path('product_category', ApiProductCategory.as_view(), name='product_category_'),
    path('marketing_category', ApiMarketingCategory.as_view(), name='marketing_category'),
]