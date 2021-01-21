"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from product.views import (
    # main page
    main,

    # search
    search,

    # marketing
    new_arrival,
    discount,
    sale_off,

    # product
    computer,
    mobile,
    tv,
    watch,
    accessories,
    product_detailed_view,
)
from order.views import (
    cart,
    add_to_cart,
    remove_from_cart,
    checkout,
    process_order,
)
from account.views import (
    account,
    shipping_address,
    login_view,
    logout_view,
    registration_view,
)

urlpatterns = [
    # main
    path('', main, name='main'),

    # search
    path('search/', search, name='search'),

    # catalog
    path('computer/', computer, name='computer'),
    path('mobile/', mobile, name='mobile'),
    path('tv/', tv, name='tv'),
    path('watch/', watch, name='watch'),
    path('accessories/', accessories, name='accessories'),


    # detailed view
    path('product/<slug:slug>/', product_detailed_view, name='product_detailed_view'),

    # marketing 
    path('new_arrival/', new_arrival, name='new_arrival'),
    path('discount/', discount, name='discount'),
    path('sale_off/', sale_off, name='sale_off'),

    # account
    path('account/', account, name='account'),
    path('shipping_address/', shipping_address, name='shipping_address'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),

    # cart
    path('cart/', cart, name='cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:id>', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('process_order/', process_order, name='process_order'),

    # rest_framework urls
    path('api/product/', include('product.api.urls')),
    path('api/mobile/', include('mobile.api.urls')),
    path('api/account/', include('account.api.urls')),
    path('api/order/', include('order.api.urls')),

    # admin
    path('admin/', admin.site.urls)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
