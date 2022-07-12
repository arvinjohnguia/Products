from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('shop/', views.shop, name="shop"),
    path('shop/<str:pk>/', views.shopIndivProduct, name="shop-individual-product"),
    
    path('products/', views.products, name="products"),
    path('products/<str:pk>/', views.indivProduct, name="individual-product"),

    path('create-product/', views.createProduct, name="create-product"),
    path('update-product/<str:pk>/', views.updateProduct, name="update-product"),
    path('delete-product/<str:pk>/', views.deleteProduct, name="delete-product"),

]