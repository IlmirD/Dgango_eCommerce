from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from product.models import Product
from product.api.serializers import ProductSerializer

# product
@api_view(['GET', ])
def product_list(request):
    if request.method == 'GET':
        product = Product.objects.order_by('-published')
        serializer = ProductSerializer(product, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

class Paginator(PageNumberPagination):
    page_size_query_param = 'page_size'

# MARKETING
class ApiMarketing(ListAPIView):
    queryset = Product.objects.filter(marketing=True)
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = Paginator
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description')

# new arrival
class ApiNewArrivalListView(ListAPIView):
    queryset = Product.objects.filter(new_arrival=True)
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = Paginator

# discount
class ApiDiscountListView(ListAPIView):
    queryset = Product.objects.filter(discount=True)
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = Paginator

# sale_off
class ApiSaleOffListView(ListAPIView):
    queryset = Product.objects.filter(sale_off=True)
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = Paginator

 # PRODUCT
# for all product
class ApiProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = Paginator
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description')

# for computers
class ApiComputerListView(ListAPIView):
    queryset = Product.objects.filter(category='Computers')
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = Paginator
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description')

# for mobile
class ApiMobileListView(ListAPIView):
    queryset = Product.objects.filter(category='Mobiles')
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = Paginator
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description')

# for tvs
class ApiTVListView(ListAPIView):
    queryset = Product.objects.filter(category='TVs')
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = Paginator
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description')

# for watch
class ApiWatchListView(ListAPIView):
    queryset = Product.objects.filter(category='Watches')
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = Paginator
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description')

# for Accesories
class ApiAccessoriesListView(ListAPIView):
    queryset = Product.objects.filter(category='Accessories')
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = Paginator
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description')
