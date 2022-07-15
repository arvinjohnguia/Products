from django.shortcuts import redirect, render
from django.db.models import Q
from django.core.paginator import Paginator

from .models import insProduct, otcProduct, ProductType, Category 
from .forms import otcProductForm, insProductForm #, StatusForm

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

# OTC PRODUCTS ------------------------------------------------------
def shop(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = otcProduct.active_objects.filter(
        Q(ProdType_Name__ProdType_Name__icontains=q) |
        Q(Cat_Name__Cat_Name__icontains=q) |
        Q(Prod_Name__icontains=q) 
    ).order_by('-date_created')

    prod_type = ProductType.objects.all()
    categories = Category.objects.all()

    #PAGE NAVIGATION
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_prod = paginator.get_page(page_number)

    context= {'prod_type': prod_type, 'categories': categories, 'products': products, 'page_prod': page_prod}
    return render(request, 'base/otc-products/shop.html', context)

def shopIndivProduct(request, pk):
    product = otcProduct.objects.get(id=pk)

    #BROWSE OTHER PRODUCTS
    browse = otcProduct.objects.filter(Cat_Name=product.Cat_Name).order_by('?').exclude(id=pk)
        #.filter(ProdType_Name=product.ProdType_Name)
        
    context = {'product': product, 'browse': browse}
    return render(request, 'base/otc-products/shop_indiv_product.html', context)

def otcProducts(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = otcProduct.objects.all()
    
    search = otcProduct.objects.filter(
        Q(id__icontains=q) |
        Q(Prod_Name__icontains=q) |
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
    return render(request, 'base/otc-products/products.html', context)

def otc_indivProduct(request, pk):
    product = otcProduct.objects.get(id=pk)

    context = {'product': product}
    return render(request, 'base/otc-products/indiv_product.html', context)

def otc_createProduct(request):
    form = otcProductForm()
    if request.method == 'POST':
        form = otcProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('otc-products')

    context = {'form': form}
    return render(request, 'base/otc-products/product_form.html', context)

def otc_updateProduct(request, pk):
    product = otcProduct.objects.get(id=pk)
    form = otcProductForm(instance=product)

    if request.method == 'POST':
        form = otcProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('otc-products')

    context = {'form': form}
    return render(request, 'base/otc-products/product_form.html', context)

#def deleteProduct(request, pk):
#    product = otcProduct.objects.get(id=pk)
#    if request.method == 'POST':
#        product.delete()
#        return redirect('products')

#    return render(request, 'base/delete_product.html', {'obj': product})


# INSALON PRODUCTS ------------------------------------------------------
def insProducts(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = insProduct.objects.all()
    
    search = insProduct.objects.filter(
        Q(id__icontains=q) |
        Q(Prod_Name__icontains=q) |
        Q(ProdType_Name__ProdType_Name__icontains=q) |
        Q(Cat_Name__Cat_Name__icontains=q) 
    ).order_by('-date_created')
    
    #PAGE NAVIGATION
    paginator = Paginator(search, 10)
    page_number = request.GET.get('page')
    page_prod = paginator.get_page(page_number)

    context = {'products': products, 'search': search, 'page_prod': page_prod}
    return render(request, 'base/ins-products/products.html', context)

def ins_indivProduct(request, pk):
    product = insProduct.objects.get(id=pk)

    context = {'product': product}
    return render(request, 'base/ins-products/indiv_product.html', context)

def ins_createProduct(request):
    form = insProductForm()
    if request.method == 'POST':
        form = insProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ins-products')

    context = {'form': form}
    return render(request, 'base/ins-products/product_form.html', context)

def ins_updateProduct(request, pk):
    product = insProduct.objects.get(id=pk)
    form = insProductForm(instance=product)

    if request.method == 'POST':
        form = insProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('ins-products')

    context = {'form': form}
    return render(request, 'base/ins-products/product_form.html', context)
