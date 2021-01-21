from django.urls import path


from product.api.views import (
    ApiMarketing,
    ApiNewArrivalListView,
    ApiDiscountListView,
    ApiSaleOffListView,

    ApiProductListView,
    ApiComputerListView,
    ApiMobileListView,
    ApiTVListView,
    ApiWatchListView,
    ApiAccessoriesListView,
)

urlpatterns = [
    path('Marketing', ApiMarketing.as_view(), name='Marketing_'),
    path('New_arrival', ApiNewArrivalListView.as_view(), name='New_arrival_'),
    path('Discount', ApiDiscountListView.as_view(), name='Discount_'),
    path('Sale_off', ApiSaleOffListView.as_view(), name='Sale_off_'),

    # product
    path('List', ApiProductListView.as_view(), name='List_'),
    path('Computers', ApiComputerListView.as_view(), name='Computer_'),
    path('Mobiles', ApiMobileListView.as_view(), name='Mobile_'),
    path('TVs', ApiTVListView.as_view(), name='TVs_'),
    path('Watches', ApiWatchListView.as_view(), name='Watches_'),
    path('Accessories', ApiAccessoriesListView.as_view(), name='Accessories_'),
]