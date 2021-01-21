from django.urls import path

from order.api.views import ApiOrder, ApiCart, AddToCart, RemoveFromCart, IncreaseQuantity, DecreaseQuantity

urlpatterns = [
    path('order_list', ApiOrder.as_view() , name='order_list_'),
    path('cart_list', ApiCart.as_view() , name='cart_list_'), 
    path('add_to_cart', AddToCart.as_view() , name='add_to_cart_'),
    path('remove_from_cart', RemoveFromCart.as_view() , name='remove_from_cart_'),
    path('increase_quantity', IncreaseQuantity.as_view() , name='increase_quantity_'),
    path('decrease_quantity', DecreaseQuantity.as_view() , name='decrease_quantity_'),
]