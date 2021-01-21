from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from mobile.models import ProductCategory, MarketingCategory
from mobile.api.serializers import ProductCategorySerializer, MarketingCategorySerializer

@api_view(['GET', ])
def product_category(request):
    if request.method == 'GET':
        product_category = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(product_category, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET', ])
def marketing_category(request):
    if request.method == 'GET':
        marketing_category = MarketingCategory.objects.all()
        serializer = MarketingCategorySerializer(marketing_category, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)


class ApiProductCategory(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

class ApiMarketingCategory(ListAPIView):
    queryset = MarketingCategory.objects.all()
    serializer_class = MarketingCategorySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )