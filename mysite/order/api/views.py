from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
import json

from order.models import Order, OrderItem
from order.api.serializers import OrderSerializer

from product.models import Product
from account.models import Account

class Paginator(PageNumberPagination):
    page_size_query_param = 'page_size'

class ApiOrder(ListAPIView, Paginator):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if request.method == 'GET':
            email = request.headers.get('email')
            customer = Account.objects.get(email=email)
            order = Order.objects.filter(customer=customer, complete=True)
            order_list = self.paginate_queryset(order)
            serializer = OrderSerializer(order_list, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

class ApiCart(ListAPIView, Paginator):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if request.method == 'GET':
            email = request.headers.get('email')
            customer = Account.objects.get(email=email)
            cart = Order.objects.filter(customer=customer, complete=False)
            serializer = OrderSerializer(cart, many=True, context={'request': request})
            return JsonResponse(serializer.data, safe=False)

class AddToCart(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        if request.method == 'POST':
            request.session.set_expiry(120000)
            
            data = request.POST
            product_id = data.get('product_id')
            email = data.get('email')
            customer = Account.objects.get(email=email)

            product = Product.objects.get(id=product_id)

            try:
                order = Order.objects.get(customer=customer, complete=False)
            except:
                order = Order.objects.create(customer=customer, complete=False)
            
            order_item, created = OrderItem.objects.get_or_create(order=order, product=product, quantity=1)

            order_item.save()

            request.session['items_total'] = order.order_item.count()

            return JsonResponse({'Product': 'Product was added'})

class RemoveFromCart(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        if request.method == 'POST':
            data = request.POST
            product_id = data.get('product_id')
            email = data.get('email')

            customer = Account.objects.get(email=email)
            order = Order.objects.get(customer=customer, complete=False)

            orderitem = OrderItem.objects.get(order=order, product=product_id)
            orderitem.order = None
            orderitem.save()
            
            return JsonResponse({'Product': 'Product was removed'})

class IncreaseQuantity(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        if request.method == 'POST':
            data = request.POST
            product_id = data.get('product_id')
            email = data.get('email')

            customer = Account.objects.get(email=email)
            order = Order.objects.get(customer=customer, complete=False)

            product = Product.objects.get(id=product_id)
            order_item = OrderItem.objects.get(order=order, product=product)
            order_item.quantity = (order_item.quantity + 1)
            order_item.save()

            return JsonResponse({'Product': 'Quantity increased'})

class DecreaseQuantity(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        if request.method == 'POST':
            data = request.POST
            product_id = data.get('product_id')
            email = data.get('email')

            customer = Account.objects.get(email=email)
            order = Order.objects.get(customer=customer, complete=False)

            product = Product.objects.get(id=product_id)
            order_item = OrderItem.objects.get(order=order, product=product)
            if order_item.quantity != 1:
                order_item.quantity = (order_item.quantity - 1)
                order_item.save()

            return JsonResponse({'Product': 'Quantity decreased'})
    
