from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm

from .models import Account
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from product.models import Product
from order.models import Order

from django.db.models import Q

import json

@login_required
def account(request):
    try:
        customer = request.user
        print(customer.id)
        orders = Order.objects.filter(customer=customer, complete=True).order_by('-date_ordered')
        context = {'orders': orders}
    except:
        context = {}

    return render(request, 'account/account.html', context)

# Shipping address
def shipping_address(request):
    data = json.loads(request.body)

    Account.objects.update(
        region = data['shipping']['region'],
        district = data['shipping']['district'],
        city = data['shipping']['city'],
        zip_code = data['shipping']['zipcode'],
        street = data['shipping']['street'],
        house = data['shipping']['house'],
    )

    return JsonResponse('Data saved', safe=False)


def registration_view(request):
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('main')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context = {'registration_form': form}
    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('main')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('main')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                return redirect('main')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)
