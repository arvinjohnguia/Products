from django.shortcuts import redirect, render
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Product, ProductType, Category
from .forms import ProductForm #, StatusForm

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def shop(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.active_objects.filter(
        Q(ProdType_Name__ProdType_Name__icontains=q) |
        Q(Cat_Name__Cat_Name__icontains=q) |
        Q(insProd_Name__icontains=q) 
    ).order_by('-date_created')

    prod_type = ProductType.objects.all()
    categories = Category.objects.all()

    #PAGE NAVIGATION
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_prod = paginator.get_page(page_number)

    context= {'prod_type': prod_type, 'categories': categories, 'products': products, 'page_prod': page_prod}
    return render(request, 'base/shop.html', context)

def shopIndivProduct(request, pk):
    product = Product.objects.get(id=pk)

    #BROWSE OTHER PRODUCTS
    browse = Product.objects.filter(Cat_Name=product.Cat_Name).order_by('?').exclude(id=pk)
        #.filter(ProdType_Name=product.ProdType_Name)
        
    context = {'product': product, 'browse': browse}
    return render(request, 'base/shop_indiv_product.html', context)

def products(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.all()
    
    search = Product.objects.filter(
        Q(id__icontains=q) |
        Q(insProd_Name__icontains=q) |
        Q(ProdType_Name__ProdType_Name__icontains=q) |
        Q(Cat_Name__Cat_Name__icontains=q) 
    ).order_by('-date_created')
    
    #form = StatusForm()
    #if request.method == 'POST':
    #    form = StatusForm(request.POST)
    #    if form.is_valid():
    #        form.save()

    #PAGE NAVIGATION
    paginator = Paginator(search, 10)
    page_number = request.GET.get('page')
    page_prod = paginator.get_page(page_number)

    context = {'products': products, 'search': search, 'page_prod': page_prod}
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