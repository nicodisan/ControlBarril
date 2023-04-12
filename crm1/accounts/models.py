from django.db import models

# Create your models here.


class Cliente(models.Model):

    LISTA_PRECIOS = (
        ('Precio1', 'Precio 1'),
        ('Precio2', 'Precio 2'),
        ('Precio3', 'Precio 3')
    )

    nombre = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=20, null=True)
    vendedor = models.CharField(max_length=30, null=True)
    lista_precios = models.CharField(max_length=30, null=True, choices=LISTA_PRECIOS)

    def __str__(self):
        return self.nombre
        
class Estilo(models.Model):

    nombre_estilo = models.CharField(max_length=20, null=True)
    precio1 = models.FloatField(null=True, blank=True)
    precio2 = models.FloatField(null=True, blank=True)
    precio3 = models.FloatField(null=True, blank=True)
   

    def __str__(self):
        return self.nombre_estilo


class Lote(models.Model):

    num_lote = models.CharField(max_length=20, null=True)
    fecha_lote = models.DateField(null=True)
    estilo = models.ForeignKey(Estilo, null=True, blank=True, on_delete= models.SET_NULL)
  
    def __str__(self):
        return self.num_lote

class Barril(models.Model):
   
    num_barril = models.CharField(max_length=20, null=True)
    precio = models.FloatField(null=True, blank=True)
    estilo = models.ForeignKey(Estilo, null=True, blank=True, on_delete= models.SET_NULL)
    lote = models.ForeignKey(Lote, null=True, blank=True, on_delete= models.SET_NULL)
    ubicacion = models.ForeignKey(Cliente, null=True, on_delete= models.SET_NULL)
    volumen = models.CharField(max_length=3, null=True)
    estado_actual = models.ForeignKey("Embarrilado", related_name='barriles', null=True, blank=True, on_delete=models.SET_NULL)
    
   

    def __str__(self):
        return self.num_barril



class Embarrilado(models.Model):

    lote = models.ForeignKey(Lote, null=True, blank=True, on_delete= models.SET_NULL)
    ubicacion = models.ForeignKey(Cliente, null=True, on_delete= models.SET_NULL)
    num_barril = models.ForeignKey(Barril, null=True, on_delete= models.SET_NULL)
    date_created = models.DateField(null=True)
    

    def __str__(self):
        return str(self.lote)



