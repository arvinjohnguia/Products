from django.shortcuts import redirect, render
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm, StatusForm

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def shop(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.active_objects.filter(
        Q(Cat_Name__Cat_Name__icontains=q) |
        Q(insProd_Name__icontains=q) 
    )

    categories = Category.objects.all()
    
    context= {'categories': categories, 'products': products}
    return render(request, 'base/shop.html', context)

def shopIndivProduct(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'base/shop_indiv_product.html', context)

def products(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.all()
    
    search = Product.objects.filter(
        Q(Cat_Name__Cat_Name__icontains=q) |
        Q(id__icontains=q) |
        Q(insProd_Name__icontains=q)
    )
    
    form = StatusForm()
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'products': products, 'products': search, 'form': form}
    return render(request, 'base/products.html', context)

def indivProduct(request, pk):
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
        form = ProductForm(request.POST, request.FILES, instance=product)
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