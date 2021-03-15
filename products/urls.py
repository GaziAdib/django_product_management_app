from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowAllProducts, name='showProducts'),
    path('product/<int:pk>/', views.productDetail, name='product'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('updateProduct/<int:pk>/', views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name='deleteProduct'),
     path('search/', views.searchBar, name='search'),
    
]