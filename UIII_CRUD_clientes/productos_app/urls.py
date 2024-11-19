from django.urls import path
from productos_app import views  

urlpatterns = [
    path('', views.inicio_vista, name='inicio'),  
    path('registrarProducto/', views.registrarProducto, name='registrarProducto'),
    path('borrarProducto/<idproducto>/', views.borrarProducto, name='borrarProducto'),
    path('seleccionarProducto/<idproducto>/', views.seleccionarProducto, name='seleccionarProducto'),
    path('editarProducto/', views.editarProducto, name='editarProducto')
]
