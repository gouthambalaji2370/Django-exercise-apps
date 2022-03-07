from django.shortcuts import render


# Create your views here.

def electronics(request):
    product_dict = {
        'heading': 'Electronics',
        'product1': 'Mac',
        'product2': 'Dell',
        'product3': 'Lenovo',
        'image': "mac.jpeg"
    }
    return render(request, 'productApp/products.html', product_dict)


def shoes(request):
    product_dict = {
        'heading': 'Shoes',
        'product1': 'Nike',
        'product2': 'Adidas',
        'product3': 'Reebok',
        'image': "nike.jpg"

    }
    return render(request, 'productApp/products.html', product_dict)


def toys(request):
    product_dict = {
        'heading':'Toys',
        'product1': 'remote car',
        'product2': 'drone',
        'product3': 'rocket',
        'image': "toys-car.jpeg"
    }
    return render(request, 'productApp/products.html', product_dict)


def index(request):
    return render(request, 'productApp/index.html')
