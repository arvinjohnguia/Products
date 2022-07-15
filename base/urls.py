from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('shop/', views.shop, name="shop"),
    path('shop/<str:pk>/', views.shopIndivProduct, name="shop-individual-product"),
    
    #INSALON PRODUCTS
    path('ins/products/', views.insProducts, name="ins-products"),
    path('ins/products/<str:pk>/', views.ins_indivProduct, name="ins-individual-product"),

    path('ins/create-product/', views.ins_createProduct, name="ins-create-product"),
    path('ins/update-product/<str:pk>/', views.ins_updateProduct, name="ins-update-product"),

    #OTC PRODUCTS
    path('otc/products/', views.otcProducts, name="otc-products"),
    path('otc/products/<str:pk>/', views.otc_indivProduct, name="otc-individual-product"),

    path('otc/create-product/', views.otc_createProduct, name="otc-create-product"),
    path('otc/update-product/<str:pk>/', views.otc_updateProduct, name="otc-update-product"),
    #path('delete-product/<str:pk>/', views.deleteProduct, name="delete-product"),

]