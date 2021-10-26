from django.shortcuts import render
from products.models import Product

# Create your views here.



def all_data(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {"all_products":all_products})


def get_one(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'index.html', {"all_products": [product]})


def filter_recs(request):
    filtered_data = Product.objects.filter(brand__iexact="Philips").order_by('-warranty')
    return render(request, 'index.html', {"all_products": filtered_data})

def exclude_data(request):
    filtered_data = Product.objects.exclude(brand="Samsung")
    return render(request, 'index.html', {"all_products": filtered_data})


def order_data(request):
    filtered_data = Product.objects.order_by('-price')
    return render(request, 'index.html', {"all_products": filtered_data})

def look_up(request):
    look_up_data = Product.objects.filter(delivery__in=["India", "france"])
    return render(request, 'index.html', {"all_products": look_up_data})

# def distinct_data(request):
#     distinct_d = Product.objects.order_by('price').distinct('brand')
#     return render(request, 'index.html', {"all_products": distinct_d})


def manager_demo(request):
    distinct_d = Product.objects.apply_seasonal_discount(0.10)
    # distinct_d = Product.objects.get_taxed_prices()
    return render(request, 'index.html', {"all_products": distinct_d})