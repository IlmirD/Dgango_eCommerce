from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage, ViewedProduct, NewArrival, Discount, SaleOff
from .forms import CommentForm

from datetime import datetime

# Search
from django.db.models import Q

# Pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

PRODUCT_PER_PAGE = 4

def search(request):
    product = Product.objects.all()

    try:
        q = request.GET.get('q')
    except:
        q = None
    
    if q:
        q = q.strip()
        product = product.filter(Q(name__icontains=q) | Q(description__icontains=q)).distinct()

    context = {'product': product, 'query': q }

    return render(request, 'product/search.html', context)

# Main
def main(request):
    new_arrival = NewArrival.objects.all()
    discount = Discount.objects.all()
    sale_off = SaleOff.objects.all()
    # Marketing
    try :
        marketing = Product.objects.filter(marketing=True)
    except:
        context = {}

    context = { 
        'marketing': marketing,
        'new_arrival': new_arrival,
        'discount': discount,
        'sale_off': sale_off,
    }

    return render(request, 'product/main.html', context)

def new_arrival(request):
    try :
        new_arrival = Product.objects.filter(new_arrival=True)
    except:
        context = {}
    
    # Pagination
    page = request.GET.get('page', 1)
    product_paginator = Paginator(new_arrival, PRODUCT_PER_PAGE)

    try:
        new_arrival = product_paginator.page(page)
    except PageNotAnInteger:
        new_arrival = product_paginator.page(PRODUCT_PER_PAGE)
    except EmptyPage:
        new_arrival = product_paginator.page(product_paginator.num_pages)
    
    context = {
        'new_arrival': new_arrival,
    }

    return render(request, 'product/marketing/new_arrival.html', context)

def discount(request):
    try:
        discount = Product.objects.filter(discount=True)
    except:
        context = {}
       
    # Pagination
    page = request.GET.get('page', 1)
    product_paginator = Paginator(discount, PRODUCT_PER_PAGE)

    try:
        discount = product_paginator.page(page)
    except PageNotAnInteger:
        discount = product_paginator.page(PRODUCT_PER_PAGE)
    except EmptyPage:
        discount = product_paginator.page(product_paginator.num_pages)
    
    context = {
        'discount': discount,
    }

    return render(request, 'product/marketing/discount.html', context)

def sale_off(request):
    try :
        sale_off = Product.objects.filter(sale_off=True)
    except:
        context = {}
    
    # Pagination
    page = request.GET.get('page', 1)
    product_paginator = Paginator(sale_off, PRODUCT_PER_PAGE)

    try:
        sale_off = product_paginator.page(page)
    except PageNotAnInteger:
        sale_off = product_paginator.page(PRODUCT_PER_PAGE)
    except EmptyPage:
        sale_off = product_paginator.page(product_paginator.num_pages)

    context = {
        'sale_off': sale_off,
    }

    return render(request, 'product/marketing/sale_off.html', context)


# computer
def computer(request):
    try :
        product = Product.objects.filter(category='Computers')
    except:
        context = {}

    # Filter
    if request.GET.get('name'):
        product = product.order_by('name')
    if request.GET.get('l2h'):
        product = product.order_by('price')
    if request.GET.get('h2l'):
        product = product.order_by('-price')

    # Pagination
    page = request.GET.get('page', 1)
    product_paginator = Paginator(product, PRODUCT_PER_PAGE)

    try:
        product = product_paginator.page(page)
    except PageNotAnInteger:
        product = product_paginator.page(PRODUCT_PER_PAGE)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)
    
    context = {'product': product}

    return render(request, 'product/category/product.html', context)


# mobile
def mobile(request):
    try :
        product = Product.objects.filter(category='Mobiles')
    except:
        context = {}

    # Filter
    if request.GET.get('name'):
        product = product.order_by('name')
    if request.GET.get('l2h'):
        product = product.order_by('price')
    if request.GET.get('h2l'):
        product = product.order_by('-price')

    # Pagination
    page = request.GET.get('page', 1)
    product_paginator = Paginator(product, PRODUCT_PER_PAGE)

    try:
        product = product_paginator.page(page)
    except PageNotAnInteger:
        product = product_paginator.page(PRODUCT_PER_PAGE)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)

    context = {'product': product}

    return render(request, 'product/category/product.html', context)


# tv
def tv(request):
    try:
        product = Product.objects.filter(category='TVs')
    except:
        context = {}

    # Filter
    if request.GET.get('name'):
        product = product.order_by('name')
    if request.GET.get('l2h'):
        product = product.order_by('price')
    if request.GET.get('h2l'):
        product = product.order_by('-price')

    # Pagination
    page = request.GET.get('page', 1)
    product_paginator = Paginator(product, PRODUCT_PER_PAGE)

    try:
        product = product_paginator.page(page)
    except PageNotAnInteger:
        product = product_paginator.page(PRODUCT_PER_PAGE)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)

    context = {'product': product}

    return render(request, 'product/category/product.html', context)

# watch
def watch(request):
    try:
        product = Product.objects.filter(category='Watches')
    except:
        context = {}

    # Filter
    if request.GET.get('name'):
        product = product.order_by('name')
    if request.GET.get('l2h'):
        product = product.order_by('price')
    if request.GET.get('h2l'):
        product = product.order_by('-price')

    # Pagination
    page = request.GET.get('page', 1)
    product_paginator = Paginator(product, PRODUCT_PER_PAGE)

    try:
        product = product_paginator.page(page)
    except PageNotAnInteger:
        product = product_paginator.page(PRODUCT_PER_PAGE)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)

    context = {'product': product}

    return render(request, 'product/category/product.html', context)

# accessories
def accessories(request):
    try:
        product = Product.objects.filter(category='Accessories')
    except:
        context = {}

    # Filter
    if request.GET.get('name'):
        product = product.order_by('name')
    if request.GET.get('l2h'):
        product = product.order_by('price')
    if request.GET.get('h2l'):
        product = product.order_by('-price')

    # Pagination
    page = request.GET.get('page', 1)
    product_paginator = Paginator(product, PRODUCT_PER_PAGE)

    try:
        product = product_paginator.page(page)
    except PageNotAnInteger:
        product = product_paginator.page(PRODUCT_PER_PAGE)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)

    context = {'product': product}

    return render(request, 'product/category/product.html', context)


# Detailed view
def product_detailed_view(request, slug):
    request.session.set_expiry(120000)

    product = get_object_or_404(Product, slug=slug)
    photos = ProductImage.objects.filter(product_detailed=product)
    
    # Comment section
    comments = product.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current product to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # for recent viewed products
    products = Product.objects.all()

    viewed_product = None
    session = request.session.session_key
    if request.user.is_authenticated:
        customer = request.user
        try:
            viewed_product = ViewedProduct.objects.get_or_create(viewed_product=product, 
                                                                customer=customer, date=datetime.now())
            viewed_product.save()
        except:
            viewed_product = None
    else:
        viewed_product = ViewedProduct.objects.get_or_create(viewed_product=product, 
                                                            session=session, date=datetime.now())

    if request.user.is_authenticated:
        viewed_product = ViewedProduct.objects.filter(customer=customer).order_by('-date')[:5]
    else:
        viewed_product = ViewedProduct.objects.filter(session=session).order_by('-date')[:5]

    context = {
        'product': product,
        'photos': photos, 
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'viewed_product': viewed_product,
        'products': products,
        
    }

    return render(request, 'product/category/product_detailed_view.html', context)
