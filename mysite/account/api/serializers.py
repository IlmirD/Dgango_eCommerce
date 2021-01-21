from rest_framework import serializers
from rest_framework.response import Response

from account.models import Account

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        account = Account(
            username = self.validated_data['username'],
            email=self.validated_data['email'],
        )
        check_account = Account.objects.filter(username=self.validated_data['email']).first()
        if check_account is not None:
            return Response ({'email': 'account with this email already exists.'})
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли должны совпадать.'})
        account.set_password(password)
        account.save()
        return account

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'username', 'region', 'district', 'city', 'zip_code', 'street', 'house',
        ]