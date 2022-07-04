from django.shortcuts import redirect, render
from django.db.models import Q

from .models import Product
from .forms import ProductForm

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def products(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.all()
    search = Product.objects.filter(
        Q(id__icontains=q) |
        Q(insProd_Name__icontains=q)
    )
    context = {'products': products, 'products': search}
    return render(request, 'base/products.html', context)

def indivproduct(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'base/indiv_product.html', context)

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form}
    return render(request, 'base/product_form.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form}
    return render(request, 'base/product_form.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')

    return render(request, 'base/delete_product.html', {'obj': product})