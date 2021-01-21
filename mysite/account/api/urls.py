from django.urls import path
from account.api.views import registration_view, ShippingAddress

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', registration_view, name='register_'),
    path('login', obtain_auth_token, name='login_'),
    path('shipping_address', ShippingAddress.as_view(), name='shipping_address_'),
]