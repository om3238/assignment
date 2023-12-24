import json
from django.shortcuts import render
from .models import Products
import json
import requests

def fetch_and_store_data(request):
    json_url = 'https://s3.amazonaws.com/open-to-cors/assignment.json'

    response = requests.get(json_url)

    if response.status_code == 200:
        data = response.json().get('products')
        products_list = []
        for products_id, product_info in data.items():
            product = Products(
                product_id = products_id,
                subcategory=product_info.get('subcategory'),
                title=product_info.get('title'),
                price=product_info.get('price'),
                popularity=product_info.get('popularity')
            )
            products_list.append(product)

        Products.objects.bulk_create(products_list)

        all_products = Products.objects.all()
    else:
        all_products = []

    return render(request,'display.html',{'all_products': all_products})
