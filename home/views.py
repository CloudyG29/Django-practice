from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Product, Stock

# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request,'home/index.html',{'products':products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'home/product_detail.html', {'product': product})