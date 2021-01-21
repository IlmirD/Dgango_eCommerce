from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter

from account.api.serializers import RegistrationSerializer, ShippingAddressSerializer
from account.models import Account

@api_view(['POST', ])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'Регистрация прошла успешно.'
    else:
        data = serializer.errors
    return Response(data)

class ShippingAddress(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if request.method == 'GET':
            email = request.headers.get('email')
            shipping_address = Account.objects.filter(email=email)
            serializer = ShippingAddressSerializer(shipping_address, many=True, context={'request': request})
            return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        if request.method == 'POST':
            data = request.POST
            email = data.get('email')

            account = Account.objects.filter(email=email)

            account.update(
                region = data.get('region'),
                district =  data.get('district'),
                city =  data.get('city'),
                zip_code =  data.get('zip_code'),
                street =  data.get('street'),
                house =  data.get('house'),
            )
            
            return JsonResponse({'Address': 'Shipping address changed'})