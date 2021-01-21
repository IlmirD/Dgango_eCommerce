import json
import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.db.models.fields import FloatField

from .models import Order, OrderItem, ShippingAddress

from product.models import Product

# Search
from django.db.models import Q


# CART
def cart(request):
    try:
        the_id = request.session['order_id']
    except:
        the_id = None

    if request.user.is_authenticated:
        customer = request.user
        try:
            order = Order.objects.get(customer=customer, complete=False)
        except:
            order = None
    else:
        try:
            order = Order.objects.get(id=the_id, complete=False)
        except:
            order = None
    
    try:
        data = request.POST
        product_id = data.get('product_id')
        action = data.get('action')
    except:
        pass
    
    if action:
        product = Product.objects.get(id=product_id)
        order_item = OrderItem.objects.get(order=order, product=product)
        if action == 'add':
            order_item.quantity = (order_item.quantity + 1)
        if action == 'remove' and order_item.quantity != 1:
            order_item.quantity = (order_item.quantity - 1)
        order_item.save()

    if order is not None:
        new_total = 0
        for item in order.order_item.all():
            line_total = item.product.price * item.quantity
            new_total += line_total
        order.total = new_total
        order.save()
        request.session['items_total'] = order.order_item.count()
    else:
        context = {}
    
    context = {'order': order}

    return render(request, 'order/cart.html', context)


def add_to_cart(request):
    request.session.set_expiry(120000)
    return_dict = dict()

    try:
        the_id = request.session['order_id']
    except:
        new_order = Order()
        new_order.save()
        request.session['order_id'] = new_order.id
        the_id = new_order.id
    
    data = request.POST
    product_id = data.get('product_id')

    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        customer = request.user
        try:
            order = Order.objects.get(customer=customer, complete=False)
        except:
            order = Order.objects.create(customer=customer, complete=False)
    else:
        order = Order.objects.get(id=the_id, complete=False)
    
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product, quantity=1)

    order_item.save()

    request.session['items_total'] = order.order_item.count()
    return_dict = {'new_total': request.session['items_total']}

    return JsonResponse(return_dict)


def remove_from_cart(request, id):
    try:
        the_id = request.session['order_id']
        order = Order.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse('cart'))

    orderitem = OrderItem.objects.get(id=id)
    print(orderitem.id)

    # orderitem.delete()
    orderitem.order = None
    orderitem.save()
    return HttpResponseRedirect(reverse('cart'))


@login_required
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        try:
            order = Order.objects.get(customer=customer, complete=False)
            context = {'order': order}
        except:
            context = {}

    return render(request, 'order/checkout.html', context)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    model_field = FloatField()
    form_field = model_field.formfield(localize=True)

    customer = request.user
    order = Order.objects.get(customer=customer, complete=False)

    total = form_field.to_python(data['orderTotal']['total'])

    if total == form_field.to_python(order.total):
        order.complete = True

    order.transaction_id = transaction_id
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            region=request.user.region,
            district=request.user.district,
            city=request.user.city,
            zip_code=request.user.zip_code,
            street=request.user.street,
            house=request.user.house,
        )

    request.session['items_total'] = 0

    orderitem = OrderItem.objects.all()
    orderitem.order = None

    return JsonResponse('Payment submitted..', safe=False)
