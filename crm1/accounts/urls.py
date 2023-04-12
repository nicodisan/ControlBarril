from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    
    path('', views.home, name="home"),
    path('barriles/', views.barriles, name="barriles"),
    path('cliente/<str:pk>/', views.cliente, name="cliente"),
    path('nuevo_cliente/', views.nuevoCliente, name="nuevo_cliente"),
    path('nuevo_estilo/', views.crearEstilo, name="nuevo_estilo"),
    path('nuevo_barril/', views.crearBarril, name="nuevo_barril"),
    path('nuevo_lote_barril/', views.crearLoteBarril, name="nuevo_lote_barril"),
    path('update_barril/', views.updateBarril, name="update_barril"),

]