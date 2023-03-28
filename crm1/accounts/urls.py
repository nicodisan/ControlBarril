from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    
    path('', views.home, name="home"),
    path('barriles/', views.barriles, name="barriles"),
    path('cliente/<str:pk_test>/', views.cliente, name="cliente"),
    #path('crear_barril/', views.crearBarril, name="crear_barril"),
    path('nuevo_cliente/', views.nuevoCliente, name="nuevo_cliente"),
    path('nuevo_estilo/', views.crearEstilo, name="nuevo_estilo"),

]