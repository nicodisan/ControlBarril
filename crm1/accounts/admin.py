from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Cliente)
admin.site.register(Embarrilado)
admin.site.register(Barril)
admin.site.register(Estilo)
admin.site.register(Lote)