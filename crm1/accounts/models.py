from django.db import models

# Create your models here.


class Customer(models.Model):

    LISTA_PRECIOS = (
        ('Precio 1', 'Precio 1'),
        ('Precio 2', 'Precio 2'),
        ('Precio 3', 'Precio 3')
    )

    nombre = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=20, null=True)
    vendedor = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    lista_precios = models.CharField(max_length=30, null=True, choices=LISTA_PRECIOS)

    def __str__(self):
        return self.nombre
        
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    CATEGORY = (
        ('Golden', 'Golden'),
        ('Honey', 'Honey'),
        ('Irish Red', 'Irish Red'),
        ('Ipa Argenta', 'Ipa Argenta'),
        ('Caramel Ipa', 'Caramel Ipa'),
    )


    num_barril = models.CharField(max_length=20, null=True)
    precio = models.FloatField(null=True, blank=True)
    estilo = models.CharField(max_length=30, null=True, choices=CATEGORY, blank=True)
    lote = models.CharField(max_length=20, null=True, blank=True)
    cliente = models.CharField(max_length=20, null=True, blank=True)
    ubicacion = models.CharField(max_length=20, null=True, blank=True)
    volumen = models.CharField(max_length=3, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
   

    def __str__(self):
        return self.num_barril



class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    num_pedido = models.CharField(max_length=20, null=True)
    cliente = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    num_barril = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    

    def __str__(self):
        return self.num_pedido

